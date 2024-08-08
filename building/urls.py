from django.urls import path, include
from rest_framework import routers
from .views import *
from rest_framework import routers
from building.views.generic_viewset import *

building_router = routers.DefaultRouter()
building_router.register("viewset", BuildingViewSet)


urlpatterns = [
    path('detail/<int:pk>/', building_detail, name="building-info"),

    path('v1/list/', BuildingList.as_view()),
    path('v1/create/', BuildingCreateAPIView.as_view()),
    path('v1/detail/<int:pk>/', BuildingDetailAPIView.as_view()),
    path('v1/update/<int:pk>/', BuildingUpdateAPIView.as_view()),
    path('v1/delete/<int:pk>/', BuildingDeleteAPIView.as_view()),
]