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