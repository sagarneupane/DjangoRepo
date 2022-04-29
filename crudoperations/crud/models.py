from django.db import models

# from dateutil.relativedelta import relativedelta
# from datetime import datetime

# Create your models here.
from django.db.models import IntegerField


class Position(models.Model):
    title = models.CharField(max_length=15)

    def __str__(self):
        return self.title


class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=15)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname


class Course(models.Model):
    courseName = models.CharField(max_length=24)
    courseDetails = models.CharField(max_length=150)
    courseId = models.CharField(max_length=4)
    courseTenure = models.CharField(max_length=1)

    def __str__(self):
        return self.courseName


class Student(models.Model):
    studentName = models.CharField(max_length=24)
    studentAddress = models.CharField(max_length=32)
    birth_date = models.DateField()
    age = models.IntegerField()
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=14)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.studentName

    # @property
    # def get_age(self):
    #     return relativedelta(self.birth_date, datetime.date.now).years
    #
    # def save(self, *args, **kwargs):
    #     # self.unique_id = self.get_unique_id
    #     self.age = self.get_age
    #     super(Student, self).save(*args, **kwargs)


class Crops(models.Model):
    name = models.CharField(max_length=12)
    type = models.CharField(max_length=15)
    image = models.ImageField(upload_to="image/")
    def __str__(self):
        return self.name
