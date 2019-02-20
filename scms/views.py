from rest_framework import viewsets
from scms import models, serializers

class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows students to be viewed or edited.
    """
    queryset = models.Student.objects.all().order_by('last_name','first_name')
    serializer_class = serializers.StudentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows courses to be viewed or edited.
    """
    queryset = models.Course.objects.all().order_by('department__name','course_number')
    serializer_class = serializers.CourseSerializer


class CourseInstanceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows instances of courses to be viewed or edited.
    """
    queryset = models.CourseInstance.objects.all().order_by('course__department__name','course__course_number', 'start_date')
    serializer_class = serializers.CourseInstanceSerializer