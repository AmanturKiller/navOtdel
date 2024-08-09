from rest_framework import viewsets
from .serializers import UserSerializer
from django.shortcuts import render
from django.contrib.auth import get_user_model

User = get_user_model()



def user_detail(request, pk):
    user_object = User.objects.get(pk=pk)
    context = {'user': user_object}
    return render(request, 'user/user_detail.html', context)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def user_list(request):
    user_list = User.objects.all()
    context = {"user_list": user_list}
    return render(request, 'user/user_list.html', context)
