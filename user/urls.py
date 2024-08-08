from django.urls import path, include
from rest_framework import routers
from user.views import *

comment_router = routers.DefaultRouter()
comment_router.register("", UserViewSet)

urlpatterns = [
    path('', include(comment_router.urls)),
    path("list/", user_list, name="user-list"),
]


