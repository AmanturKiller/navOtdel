from django.shortcuts import render
from department.models import *
from department.filters import *


def department_list(request):
    department_list = Department.objects.all()
    filter_object = DepartmentFilter(
        data = request.GET,
        queryset = department_list
    )
    context = {"filter_object": filter_object}
    return render(request, 'department/list.html', context)
