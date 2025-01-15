from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.
class UserModel(AbstractBaseUser):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    