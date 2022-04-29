from django.db import models


# Create your models here.
class Students(models.Model):
    S_Name = models.CharField(max_length=55)
    S_Address = models.CharField(max_length=60)
    S_Parent = models.CharField(max_length=55)
    S_Course = models.TextField()
    S_id = models.IntegerField()
    S_description = models.CharField(max_length=12)

    def __str__(self):
        return self.S_Name


class StudentBehaviour(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    behaviourDetails = models.TextField()
    guardians_name = models.CharField(max_length=70)
    teacher_under_surviealiance = models.CharField(max_length=70)

