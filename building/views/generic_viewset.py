from rest_framework import viewsets
from building.models import Building
from building.serializers import BuildingSerializer


class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer