from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Department(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=100)
    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    parent = models.ForeignKey(
        to='self',
        verbose_name="Наследуется от",
        null=True, blank=True,
        on_delete=models.CASCADE,
    )
    manager = models.ForeignKey(
        verbose_name="Менеджер",
        to=User,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Отдел"
        verbose_name_plural = "Отделы"

    def __str__(self):
        return self.name
