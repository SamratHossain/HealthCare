from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField

User = get_user_model()

class Specialist(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Qualification(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    specialist = ArrayField(models.CharField(max_length=50), blank=True, null=True)
    DegreeName = models.CharField(blank=True,null=True,max_length=50)
    Institute = models.CharField(blank=True,null=True, max_length=50)
    Country = models.CharField(blank=True,null=True, max_length=50)
    PassingYear = models.DateField()

    def __str__(self):
        return self.DegreeName

class Experience(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    HospitalName = models.CharField(blank=True, null=True, max_length=50)
    Designation = models.CharField(blank=True, null=True, max_length=50)
    Department = models.CharField(blank=True, null=True, max_length=50)
    EmploymentPeriod = models.CharField(blank=True, null=True, max_length=50)
    CurrentlyWorking = models.BooleanField(default=False)
    From = models.DateField()
    To = models.DateField()

    def __str__(self):
        return self.Designation