from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    bio = models.TextField(null=True, blank=True, verbose_name='биография')
    photo = models.ImageField(
        upload_to='user_photos/',
        verbose_name='Фото',
        null=True,
        blank=True,
    )
    USERNAME_FIELD = 'username'
