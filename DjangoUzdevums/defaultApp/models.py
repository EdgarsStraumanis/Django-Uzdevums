from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=75)
    comment = models.CharField(max_length=200)

class Task(models.Model):
    name = models.CharField(max_length=75)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)