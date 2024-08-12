from django.shortcuts import render
from department.models import *


def department_detail(request, pk):
    department_object = Department.objects.get(pk=pk)
    context = {'department': department_object}
    return render(request, 'department/detail.html', context)