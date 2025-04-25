from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    id = models.CharField(primary_key=True)
    name = models.CharField(max_length=100)
    fathername = models.CharField(max_length=100)
    mothername = models.CharField(max_length=100)
    program = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    guardianphone = models.CharField(max_length=100)
    session = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    email = models.EmailField()
    pic = models.ImageField(upload_to='student_pics/', null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.id})"


class CourseRegister(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    code = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    credits = models.DecimalField(max_digits=4, decimal_places=2)
    semester = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    section = models.CharField(
        max_length=20,
        choices=[('Remove', 'Remove'), ('Add', 'Add')]
    )
    section_name_time = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"{self.code} - {self.title}"


class StudentProfile(models.Model):
    name = models.CharField(max_length=100)
    batch = models.IntegerField()
    program = models.CharField(max_length=200)
    pre_advising_credit_limit = models.IntegerField()
    taken_credit = models.IntegerField(default=0)
    advisor_name = models.CharField(max_length=100)
    registration_fee = models.CharField(max_length=100)
    roll = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} (Batch {self.batch})"
