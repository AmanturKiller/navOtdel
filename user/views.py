from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from django.shortcuts import render


def homepage(request):
    user_lst = User.objects.all()
    context = {'user_lst': user_lst}
    return render(request, 'homepage.html', context)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def user_list(request):
    user_list = User.objects.all()
    context = {"user_list": user_list}
    return render(request, 'user_list.html', context)
