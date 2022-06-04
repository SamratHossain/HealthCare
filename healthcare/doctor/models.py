from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from accounts.models import Doctor

User = get_user_model()

class Specialist(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Qualification(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='qualificationInfo')
    Specialist = models.CharField(max_length=50, blank=True, null=True)
    DegreeName = models.CharField(blank=True,null=True,max_length=50)
    InstituteName = models.CharField(blank=True,null=True, max_length=50)
    Country = models.CharField(blank=True,null=True, max_length=50)
    PassingYear = models.DateField()

    def __str__(self):
        return self.DegreeName


class Experience(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='experienceInfo')
    HospitalName = models.CharField(blank=True, null=True, max_length=50)
    Designation = models.CharField(blank=True, null=True, max_length=50)
    Department = models.CharField(blank=True, null=True, max_length=50)
    EmploymentPeriod = models.CharField(blank=True, null=True, max_length=50)
    CurrentlyWorking = models.BooleanField(default=False)
    From = models.CharField(blank=True, null=True,max_length=50)
    To = models.CharField(blank=True, null=True,max_length=50)
    
    def __str__(self):
        return self.Designation

class DoctorInfo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='doctorInfo')
    AvailableTime = models.CharField(max_length=100, blank=True, null=True)
    AvailableDay = models.CharField(max_length=100, blank=True, null=True)
    ConsultationFee = models.IntegerField()
    FollowUpFee = models.IntegerField()
    WithinDuration = models.CharField(max_length=100, blank=True, null=True)
    ConsultancyDuration = models.CharField(blank=True, null=True, max_length=50)
    NIDPhoto = models.ImageField(upload_to="Doctor/NidImage")   
    ProfilePhoto = models.ImageField(upload_to="Doctor/ProfileImage")   
    About = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.AvailableDay

class Review(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='reviewInfo')
    Name = models.CharField(max_length=500, null=True, blank=True)
    Rating = models.IntegerField()
    Date = models.DateField(auto_now=True)

    def __str__(self):
        return self.Name

class Category(models.Model):
    name = models.CharField(max_length=50,blank=True, null=True)
    about = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name