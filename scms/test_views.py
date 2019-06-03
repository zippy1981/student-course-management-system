from scms import models, views
from rest_framework.test import APIRequestFactory, APITestCase
from unittest import skip

class StudentTestCase(APITestCase):

    def setUp(self):
        self.request_factory = APIRequestFactory()
        self.student_view = views.StudentViewSet(action='get', kwargs={})
        models.Student.objects.create(first_name="Justin", last_name="Dearing")
        models.Student.objects.create(first_name="Bob", last_name="Smith")
        models.Student.objects.create(first_name="Tom", last_name="Smith")

    #@skip("Need to do a lot of mocking to get this working.")
    def test_get_students(self):
        response = self.request_factory.get('api/students/?format=json')
        self.assertEqual(200, response.status_code)
        self.assertEqual(3, len(response.body))

    def test_get_metadata(self):
        self.assertEqual('get', self.student_view.action)
        self.assertEqual('Student', self.student_view.get_view_name())
        self.assertEqual('API endpoint that allows students to be viewed or edited.', self.student_view.get_view_description())