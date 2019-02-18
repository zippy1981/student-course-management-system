from django.test import TestCase
from scms import models, views

class StudentTestCase(TestCase):
    def setUp(self):
        models.Student.objects.create(first_name="Justin", last_name="Dearing")
        models.Student.objects.create(first_name="Bob", last_name="Smith")
        models.Student.objects.create(first_name="Tom", last_name="Smith")

