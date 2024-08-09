from django.shortcuts import render
from building.models import Building


def building_detail(request, pk):
    building = Building.objects.get(pk=pk)
    context = {'building': building}
    return render(request, 'building/building_detail.html', context)
