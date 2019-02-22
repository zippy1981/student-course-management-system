import logging
from rest_framework import serializers
from scms import models

logger = logging.getLogger('zippysoft.scms.serializers')
logger.debug(f'In Serializers for {__name__}')

class LoggingModelSerializer(serializers.ModelSerializer):
    """
    ModelSerializer with debug logging
    """

    def create(self, validated_data):
        logger.debug(f'Creating with {validated_data}')
        return super().create(validated_data)

    def get_attribute(self, instance):
        logger.debug(f'Getting Attribute {instance}')
        return super().get_attribute(instance)

    def is_valid(self, raise_exception=False):
        logger.debug(f'Checking if data is valid in {self.__class__.__name__}. Thow: {raise_exception}')
        return super().is_valid(raise_exception=raise_exception)

    def save(self, **kwargs):
        logger.debug(f'{self.__class__.__name__}.save() with args [{kwargs}]')
        return super().save(**kwargs)

    def to_representation(self, instance):
        logger.debug(f'Calling {self.__class__.__name__}.to_representation() with {instance}')
        if hasattr(instance, 'department'):
            logger.debug(f'Department of instance is {instance.department}')
        return super().to_representation(instance)

    def to_internal_value(self, data):
        logger.debug(f'Calling {self.__class__.__name__}.to_internal_value() with {data}')
        return super().to_internal_value(data)


class StudentSerializer(LoggingModelSerializer):
    class Meta:
        model = models.Student
        fields = ('id', 'last_name', 'first_name', 'full_name')

class DepartmentSerializer(LoggingModelSerializer):
    class Meta:
        model = models.Department
        fields = ('name',)

class CourseSerializer(LoggingModelSerializer):
    department = serializers.SlugRelatedField(
        many = False,
        read_only = False,
        slug_field = 'name',
        queryset = models.Department.objects.all()
     )

    class Meta:
        model = models.Course
        fields = (
            'id', 
            'course_name', 
            'department',
            'course_number', 
            'credits')

class CourseSummarySerializer(LoggingModelSerializer):
    """
    Serializer for course summaries as a child object
    """
    department = serializers.SlugRelatedField(
        many = False,
        read_only = False,
        slug_field = 'name',
        queryset = models.Department.objects.all()
     )

    class Meta:
        model = models.Course
        fields = (
            'department',
            'course_number')

class CourseInstanceSerializer(LoggingModelSerializer):
    course = CourseSummarySerializer()
    
    def create(self, validated_data):
        pushed_course = validated_data.pop('course')
        logger.debug(f'CourseInstanceSerializer.create() looking up course info for {pushed_course}')
        department = models.Department.objects.get(name= pushed_course.department)
        course_model = models.Course.get(course_number=pushed_course.course_number, department = department.id)
        validated_data.course = course_model.id
        logger.debug('CourseInstanceSerializer.create() has modified the request json')
        return super().create(validated_data)


    class Meta:
        model = models.CourseInstance
        fields = (
            'id', 
            'course', 
            'start_date',
            'end_date',
        )
