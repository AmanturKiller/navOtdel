from django.urls import path
from department.views import *


urlpatterns = [
    path("list/", department_list, name="department-list"),
]