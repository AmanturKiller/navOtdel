from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet

comment_router = routers.DefaultRouter()
comment_router.register("", UserViewSet)

urlpatterns = [
    path('', include(comment_router.urls)),
]
