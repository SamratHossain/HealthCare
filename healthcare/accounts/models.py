from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .usermanager import AccountUserManager


class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(unique=True,blank=False, null=False, max_length=50)
    IsPatient = models.BooleanField(default=False)
    IsDoctor = models.BooleanField(default=False)
    JoinAt = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = AccountUserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email