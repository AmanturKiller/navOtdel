from department.models import Department
import django_filters

class DepartmentFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains", label="Название")
    class Meta:
        model = Department
        fields = ['name', 'parent', 'manager']