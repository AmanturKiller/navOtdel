from rest_framework import viewsets
from department.serializers import DepartmentSerializer
from department.models import Department

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer