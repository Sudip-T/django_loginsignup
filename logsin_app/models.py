from django.db import models
from django.contrib.auth.models import AbstractUser
from logsin_app.manager import UserManager      

class CustomUser(AbstractUser):
    username=None
    full_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=60, unique=True, help_text='Please enter a valid email address')
    phone_number = models.CharField(max_length=14)
    is_phone_verified = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
