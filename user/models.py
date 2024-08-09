from django.db import models
from django.contrib.auth.models import AbstractUser
# from department.models import Department
# from building.models import Building

class User(AbstractUser):
    bio = models.TextField(null=True, blank=True, verbose_name='биография')
    photo = models.ImageField(
        upload_to='user_photos/',
        verbose_name='Фото',
        null=True,
        blank=True,
    )
    USERNAME_FIELD = 'username'

    department = models.ForeignKey(
        'department.Department',
        on_delete=models.CASCADE,
        verbose_name='Отдел',
        related_name='users_list',
        null=True
    )
    building = models.ForeignKey('building.Building', on_delete=models.CASCADE, verbose_name='Объект', related_name='users_list', null=True)

    specialist = "specialist"
    senior_specialist = "senior_specialist"
    deputy_head = "deputy_head"
    supervisor = "supervisor"

    POSITION_CHOICES = [
        (specialist, "Специалист"),
        (senior_specialist, "Старший специалист"),
        (deputy_head, "Заместитель руководителя"),
        (supervisor, "Руководитель"),
    ]

    position = models.CharField(
        max_length=50,
        choices=POSITION_CHOICES,
        verbose_name="Должность",
        null=True
    )