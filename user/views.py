from django.shortcuts import render
from .models import User

def user_list(request):
    user_list = User.objects.all()
    context = {"user_list": user_list}
    return render(request, 'user_list.html', context)