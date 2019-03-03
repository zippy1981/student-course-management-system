from django.test import TestCase
from scms import models, views
from unittest import skip

class StudentTestCase(TestCase):

    def setUp(self):
        self.studentView = views.StudentViewSet(action='get', kwargs={})
        models.Student.objects.create(first_name="Justin", last_name="Dearing")
        models.Student.objects.create(first_name="Bob", last_name="Smith")
        models.Student.objects.create(first_name="Tom", last_name="Smith")

    @skip("Need to do a lot of mocking to get this working.")
    def test_get_students(self):
        self.assertEqual('Student', self.studentView.get_object())

    def test_get_metadata(self):
        self.assertEqual('get', self.studentView.action)
        self.assertEqual('Student', self.studentView.get_view_name())
        self.assertEqual('API endpoint that allows students to be viewed or edited.', self.studentView.get_view_description())