from django.test import TestCase
from scms.models import Student, Course, Department
from django.db.utils import IntegrityError

class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(first_name="Justin", last_name="Dearing")
        Student.objects.create(first_name="Tom", last_name="Smith")

    def test_students_fullName(self):
        """Animals that can speak are correctly identified"""
        justin = Student.objects.get(first_name="Justin", last_name="Dearing")
        tom = Student.objects.get(first_name="Tom", last_name="Smith")
        
        self.assertEqual(justin.fullName(), 'Justin Dearing')
        self.assertEqual(tom.fullName(), 'Tom Smith')

    def test_allow_duplicate_last_name(self):
        Student.objects.create(first_name="Bob", last_name="Smith")

    def test_no_duplicate_name(self):
        self.assertRaisesMessage(
            IntegrityError, 
            'Key (last_name, first_name)=(Dearing, Justin) already exists.',
            lambda: Student.objects.create(first_name="Justin", last_name="Dearing"))       

class CourseTestCase(TestCase):
    def setUp(self):
        mathDepartment = Department.objects.create(name='Math')
        Course.objects.create(course_name='Pre Calc', department = mathDepartment, course_number=101, credits=3)
        Course.objects.create(course_name='Calc I', department = mathDepartment, course_number=200, credits=3)
        Course.objects.create(course_name='Calc II', department = mathDepartment, course_number=201, credits=3)

    def test_course_fetch_by_number(self):
        preCalc = Course.objects.get(department__name = 'Math', course_number=101)
        calcI = Course.objects.get(department__name = 'Math', course_number=200)
        calcII = Course.objects.get(department__name = 'Math', course_number=201)

        self.assertEqual('Pre Calc', preCalc.course_name)
        self.assertEqual(3, preCalc.credits)
        self.assertEqual('Calc I', calcI.course_name)
        self.assertEqual(3, calcI.credits)
        self.assertEqual('Calc II', calcII.course_name)
        self.assertEqual(3, calcII.credits)