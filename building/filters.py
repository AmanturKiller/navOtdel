from building.models import Building
import django_filters

class BuildingFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains", label="Название объекта")
    class Meta:
        model = Building
        fields = ['name', 'manager', 'address', 'building_type']