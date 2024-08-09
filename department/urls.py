from django.urls import path
from department.views import *


urlpatterns = [
    path("list/", department_list, name="department-list"),
    path("info/<int:pk>", department_detail, name="department-detail"),
]