from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    sex = models.CharField(max_length=25)
    address = models.TextField()
    collegeCareer = models.CharField(max_length=50)