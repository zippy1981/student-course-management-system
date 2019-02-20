from django.db import models

class Student(models.Model):
    """Students enrolled in the school"""

    first_name = models.CharField(help_text='First Name', max_length=30)
    last_name = models.CharField(help_text='Last Name', max_length=30)

    class Meta:
        unique_together = (("last_name", "first_name"),)

    def full_name(self):
        """Full name"""
        return f'{self.first_name} {self.last_name}'

class Department(models.Model):
    """Academic Department"""

    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        # We need to override this to populate the drop down in the auto generated API page. 
        return self.name

class Course(models.Model):
    """Courses in the course catalog"""

    course_name = models.CharField(max_length=30, unique=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    course_number = models.DecimalField(decimal_places=0, max_digits=3, unique=True)
    credits = models.IntegerField()

    def __str__(self):
        # We need to override this to populate the drop down in the auto generated API page. 
        return f'{self.department}-{self.course_number} {self.course_name}'

    class Meta:
        unique_together = (("department", "course_number"),)

class CourseInstance(models.Model):
    """A Scheduled running of a particular coursee"""

    start_date = models.DateField(help_text='Course Start Date', verbose_name='Start Date')
    end_date = models.DateField(help_text='Course End Date', verbose_name='End Date')
    course = models.ForeignKey(Course, on_delete=models.deletion.CASCADE)

class CourseInstanceTime(models.Model):
    MON = 'MON'
    TUE = 'TUE'
    WED = 'WED'
    THU = 'THU'
    FRI = 'FRI'
    SAT = 'SAT'
    SUN = 'SUN'

    DAY_CHOICES = (
        (MON, 'Monday'),
        (TUE, 'Tuesday'),
        (WED, 'Wednesday'),
        (THU, 'Thursday'),
        (FRI, 'Friday'),
        (SAT, 'Saturday'),
        (SUN, 'Sunday')
    )

    day = models.CharField(choices=DAY_CHOICES, max_length=3)
    start_time = models.TimeField()
    end_time = models.TimeField()
    course_instance = models.ForeignKey(CourseInstance, on_delete=models.deletion.CASCADE)

class StudentCourseEnrollment(models.Model):
    """Students scheduled to take a particualr course"""
    
    course_instance = models.ForeignKey(CourseInstance,on_delete=models.deletion.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.deletion.CASCADE)

    class Meta:
        unique_together = (("course_instance", "student"),)