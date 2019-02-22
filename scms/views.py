import logging
from rest_framework import viewsets
from scms import models, serializers

logger = logging.getLogger('zippysoft.scms.views')
logger.debug(f'In Views for {__name__}')

class LoggingModelViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet with debug logging
    """

    def create(self, request, *args, **kwargs):
        logger.debug(f'In create for {self.__class__.__name__}. {request.path}')
        return super().create(request, *args, **kwargs)

    def get_serializer(self, *args, **kwargs):
        logger.debug(f'Getting serializer for {self.__class__.__name__} ({args}) [{kwargs}]')
        s = super().get_serializer(*args, **kwargs)
        return s

    def perform_create(self, serializer):
        logger.debug(f'In perform_create with {serializer}')
        return super().perform_create(serializer)

    def list(self, request, *args, **kwargs):
        logger.debug(f'In list for {__name__}. {request.path}')
        return super().list(request, *args, **kwargs)


class StudentViewSet(LoggingModelViewSet):
    """
    API endpoint that allows students to be viewed or edited.
    """
    queryset = models.Student.objects.all().order_by('last_name','first_name')
    serializer_class = serializers.StudentSerializer

class CourseViewSet(LoggingModelViewSet):
    """
    API endpoint that allows courses to be viewed or edited.
    """
    queryset = models.Course.objects.all().order_by('department__name','course_number')
    serializer_class = serializers.CourseSerializer


class CourseInstanceViewSet(LoggingModelViewSet):
    """
    API endpoint that allows instances of courses to be viewed or edited.
    """
    queryset = models.CourseInstance.objects.all().order_by('course__department__name','course__course_number', 'start_date')
    serializer_class = serializers.CourseInstanceSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)