from django.urls import path, include
from rest_framework import routers
from .views import *
from rest_framework import routers
from building.views.generic_viewset import *

building_router = routers.DefaultRouter()
building_router.register("viewset", BuildingViewSet)


urlpatterns = [
    path('detail/<int:pk>/', building_detail, name="building-info"),
    path('', include(building_router.urls)),
]