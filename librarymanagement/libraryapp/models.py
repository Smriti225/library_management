from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from .manager import UserManager

class CustomUser(AbstractUser, PermissionsMixin):
    username = None
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=10)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    address = models.CharField(max_length=50,null=True,blank=True)
    pincode = models.IntegerField()
    
    objects=UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
