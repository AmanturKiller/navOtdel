from rest_framework import viewsets
from .serializers import UserSerializer
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import get_user_model, authenticate, login, logout
from .forms import *
from django.contrib import messages


User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def user_detail(request, pk):
    user_object = User.objects.get(pk=pk)
    context = {'user': user_object}
    return render(request, 'user/user_detail.html', context)

def user_list(request):
    user_list = User.objects.all()
    context = {"user_list": user_list}
    return render(request, 'user/user_list.html', context)

def registration(request):
    context = {}
    if request.method == 'POST':
        reg_form = RegistrationForm(request.POST)
        if reg_form.is_valid():
            user_object = reg_form.save()
            password = request.POST['password']
            user_object.set_password(password)
            user_object.save()
            return redirect('/')
        return HttpResponse('Ошибка валидации')
    reg_form = RegistrationForm()
    context['reg_form'] = reg_form
    return render(request, 'profile/registration.html', context)

def signin(request):
    context = {}
    if request.method == 'POST':
        form = AuthForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Вы успешно авторизовались!')
                return redirect('/')
            messages.error(request, 'Логин и/или пароль введен не правильно, авторизация не прошла')
        else:
            messages.error(request, 'Данные не валидны')
    form = AuthForm()
    context['form'] = form
    return render(request, 'profile/signin.html', context)

def signout(request):
    logout(request)
    return redirect('/')