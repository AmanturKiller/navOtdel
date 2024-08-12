from django.urls import path, include
from rest_framework import routers
from user.views import *

user_router = routers.DefaultRouter()
user_router.register("", UserViewSet)

urlpatterns = [
    path("list/", user_list, name="user-list"),
    path('detail/<int:pk>/', user_detail, name="user-info"),
    path('', include(user_router.urls)),
]