from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Building(models.Model):
    AZS = "azs"
    NB = "nb"
    SHOP = "shop"
    STOCK = "stock"
    OFFICE = "office"

    BUILDING_TYPE_CHOICES = [
        (AZS, "АЗС"),
        (NB, "Нефтяная база"),
        (SHOP, "Магазин"),
        (STOCK, "Склад"),
        (OFFICE, "Офис"),
    ]

    name = models.CharField(max_length=50, null=False, blank=False, verbose_name="Название")
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='buildings')
    address = models.TextField(null=False, blank=False, verbose_name="Адрес")
    lat_decimal = models.DecimalField(max_digits=20, decimal_places=15, verbose_name="широта")
    lon_decimal = models.DecimalField(max_digits=20, decimal_places=15, verbose_name="долгота")
    building_type = models.CharField(
        max_length=50,
        choices=BUILDING_TYPE_CHOICES,
        verbose_name="Тип объекта"
    )

    class Meta:
        verbose_name = "Объект"
        verbose_name_plural = "Объекты"
