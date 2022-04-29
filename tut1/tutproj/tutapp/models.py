from django.db import models


# Create your models here.

class DatePicker1(models.Model):
    date_name = models.CharField(max_length=20)
    your_date = models.DateField()

    def __str__(self):
        return self.your_date


class Category(models.Model):
    Name = models.CharField(max_length=20)
    description = models.TextField


class Items(models.Model):
    Name = models.CharField(max_length=20)
    Description = models.CharField(max_length=150)
    image = models.ImageField(upload_to="items/")

    def __str__(self):
        return self.Name