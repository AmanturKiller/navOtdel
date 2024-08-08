from django.urls import path
from user.views import *


urlpatterns = [
    path("list/", user_list, name="user-list"),
]