from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .usermanager import AccountUserManager


class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(unique=True,blank=False, null=False, max_length=50)
    IsPatient = models.BooleanField(default=False)
    IsDoctor = models.BooleanField(default=False)
    IsApproved = models.BooleanField(default=False)
    JoinAt = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = AccountUserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email


class Doctor(models.Model):
    User = models.OneToOneField(UserAccount ,on_delete=models.CASCADE)
    Title = models.CharField(blank=True, null=True ,max_length=50)
    FirstName = models.CharField(blank=True, null=True, max_length=50)
    LastName = models.CharField(blank=True, null=True, max_length=50)
    Mobile = models.IntegerField(blank=True, null=True)
    Gender = models.CharField(blank=True, null=True, max_length=50)
    DateOfBirth = models.DateField()
    NidOrPassport = models.IntegerField(unique=True,blank=True, null=True)
    RegistrationNumberBMDC = models.IntegerField(unique=True,blank=True, null=True)

    def __str__(self):
        return self.FirstName + " " + self.LastName

class Patient(models.Model):
    User = models.OneToOneField(UserAccount ,on_delete=models.CASCADE)
    FirstName = models.CharField(blank=True, null=True, max_length=50)
    LastName = models.CharField(blank=True, null=True, max_length=50)
    Mobile = models.IntegerField(blank=True, null=True)
    Gender = models.CharField(blank=True, null=True, max_length=50)
    DateOfBirth = models.DateField()
    

    def __str__(self):
        return self.FirstName + " " + self.LastName