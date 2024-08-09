from django.shortcuts import render
from building.models import *
from building.filters import *


def buildings_list(request):
    buildings_list = Building.objects.all()
    filter_object = BuildingFilter(
        data = request.GET,
        queryset = buildings_list
    )
    context = {"filter_object": filter_object}
    return render(request, 'building/list.html', context)