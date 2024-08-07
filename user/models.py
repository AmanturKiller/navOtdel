from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    bio = models.TextField(null=True, blank=True, verbose_name='биография')
    USERNAME_FIELD = 'username' 
