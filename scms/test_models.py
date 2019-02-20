from django.test import TestCase
from scms import models
from django.db.utils import IntegrityError

class StudentTestCase(TestCase):
    def setUp(self):
        models.Student.objects.create(first_name="Justin", last_name="Dearing")
        models.Student.objects.create(first_name="Tom", last_name="Smith")

    def test_students_full_name(self):
        """Animals that can speak are correctly identified"""
        justin = models.Student.objects.get(first_name="Justin", last_name="Dearing")
        tom = models.Student.objects.get(first_name="Tom", last_name="Smith")
        
        self.assertEqual(justin.full_name(), 'Justin Dearing')
        self.assertEqual(tom.full_name(), 'Tom Smith')

    def test_allow_duplicate_last_name(self):
        models.Student.objects.create(first_name="Bob", last_name="Smith")

    def test_no_duplicate_name(self):
        self.assertRaisesMessage(
            IntegrityError, 
            'Key (last_name, first_name)=(Dearing, Justin) already exists.',
            lambda: models.Student.objects.create(first_name="Justin", last_name="Dearing"))       

class DepartmentTestCase(TestCase):
    
    def setUp(self):
        models.Department.objects.create(name='Math')
        models.Department.objects.create(name='Art')
        models.Department.objects.create(name='Science')

    def test_str(self):
        for dept in models.Department.objects.all():
            self.assertEqual(dept.name, f'{dept}')
            self.assertEqual(dept.name, dept.__str__())

class CourseTestCase(TestCase):
    def setUp(self):
        mathDepartment = models.Department.objects.create(name='Math')
        models.Course.objects.create(course_name='Pre Calc', department = mathDepartment, course_number=101, credits=3)
        models.Course.objects.create(course_name='Calc I', department = mathDepartment, course_number=200, credits=3)
        models.Course.objects.create(course_name='Calc II', department = mathDepartment, course_number=201, credits=3)

    def test_course_fetch_by_number(self):
        preCalc = models.Course.objects.get(department__name = 'Math', course_number=101)
        calcI = models.Course.objects.get(department__name = 'Math', course_number=200)
        calcII = models.Course.objects.get(department__name = 'Math', course_number=201)

        self.assertEqual('Pre Calc', preCalc.course_name)
        self.assertEqual(3, preCalc.credits)
        self.assertEqual('Calc I', calcI.course_name)
        self.assertEqual(3, calcI.credits)
        self.assertEqual('Calc II', calcII.course_name)
        self.assertEqual(3, calcII.credits)
    