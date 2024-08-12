from django.urls import path, include
from rest_framework import routers
from department.views import *
from .views import *

user_router = routers.DefaultRouter()
user_router.register("list", DepartmentViewSet)

urlpatterns = [
    path("list/", department_list, name="department-list"),
    path("info/<int:pk>/", department_detail, name="department-detail"),
    path('', include(user_router.urls)),
]
