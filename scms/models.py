from django.db import models

class Student(models.Model):
    """Students enrolled in the school"""

    first_name = models.CharField(help_text='First Name', max_length=30)
    last_name = models.CharField(help_text='Last Name', max_length=30)

class Course(models.Model):
    """Courses in the course catalog"""

    course_name = models.CharField(max_length=30, unique=True)
    course_number = models.DecimalField(decimal_places=0, max_digits=3, unique=True)
    credits = models.IntegerField()

class CourseInstance(models.Model):
    """A Scheduled running of a particular coursee"""

    start_date = models.DateField(help_text='Course Start Date', verbose_name='Start Date')
    end_date = models.DateField(help_text='Course Start Date', verbose_name='Start Date')
    course_id = models.ForeignKey(Course, on_delete=models.deletion.CASCADE)

class CourseInstanceTime(models.Model):

    DAY_CHOICES = (
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THU', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday'),
        ('SUN', 'Sunday')
    )

    day = models.CharField(choices=DAY_CHOICES, max_length=3)
    start_time = models.TimeField()
    end_time = models.TimeField()
    course_instance_id = models.ForeignKey(CourseInstance, on_delete=models.deletion.CASCADE)

class StudentCourseEnrollment(models.Model):
    """Students scheduled to take a particualr course"""
    
    course_instance_id = models.ForeignKey(CourseInstance,on_delete=models.deletion.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.deletion.CASCADE)