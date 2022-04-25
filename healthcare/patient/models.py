from django.db import models

# Create your models here.

class StudentModel(models.Model):
    stid = models.IntegerField(primary_key=True)
    stname = models.CharField(max_length=50)

class MarksModel(models.Model):
    marksid = models.IntegerField(primary_key=True)
    math = models.IntegerField()
    physics = models.IntegerField()
    computer = models.IntegerField()
    stid = models.ForeignKey(StudentModel,related_name='marks', on_delete=models.CASCADE)