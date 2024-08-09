from django.shortcuts import render
from building.models import *


def buildings_list(request):
    buildings_list = Building.objects.all()
    context = {"buildings": buildings_list}
    return render(request, 'building/list.html', context)

