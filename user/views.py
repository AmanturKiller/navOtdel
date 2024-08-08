from django.shortcuts import render, HttpResponse
from .models import User


def homepage(request):
    user_lst = User.objects.all()
    context = {'user_lst': user_lst}
    return render(request, 'homepage.html', context)