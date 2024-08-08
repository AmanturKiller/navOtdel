from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Building(models.Model):
    azs = "azs"
    nb = "nb"
    shop = "shop"
    stock = "stock"
    office = "office"

    name = models.CharField(max_length=50, null=False, blank=False, verbose_name="Название")
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    address = models.TextField(null=False, blank=False, verbose_name="Адрес")
    lat_decimal = models.DecimalField(max_digits=20, decimal_places=15)
    lon_decimal = models.DecimalField(max_digits=20, decimal_places=15)
    building_type_choices = {
        azs: "АЗС",
        nb: "Нефтяная база",
        shop: "Магазин",
        stock: "Склад",
        office: "Офис",
    }
    building_type = models.CharField(
        max_length=50,
        choices=building_type_choices,
        verbose_name="Тип объекта"
    )
