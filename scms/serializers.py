from rest_framework import serializers
from scms import models


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Student
        fields = ('id', 'last_name', 'first_name', 'full_name')

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Department
        #fields = ('id', 'last_name', 'first_name')

class CourseSerializer(serializers.ModelSerializer):
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

class CourseInstanceSerializer(serializers.ModelSerializer):
    department = serializers.SlugRelatedField(
        many = False,
        read_only = True,
        slug_field = 'name'
    )
    course = serializers.SlugRelatedField(
        many = False,
        read_only = False,
        slug_field = 'course_number',
        queryset = models.Course.objects.all()
    )

    class Meta:
        model = models.CourseInstance
        fields = (
            'id', 
            'department',
            'course', 
            'start_date',
            'end_date',
        )
