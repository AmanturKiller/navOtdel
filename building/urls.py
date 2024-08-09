from django.urls import path, include
from rest_framework import routers
from .views import *


urlpatterns = [
    path('detail/<int:pk>/', building_detail, name="building-info"),
]