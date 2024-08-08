from rest_framework.generics import ListAPIView, CreateAPIView, \
    UpdateAPIView, RetrieveAPIView, DestroyAPIView
from building.models import Building
from building.serializers import BuildingSerializer


class BuildingList(ListAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer


class BuildingCreateAPIView(CreateAPIView):
    serializer_class = BuildingSerializer


class BuildingDetailAPIView(RetrieveAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer


class BuildingUpdateAPIView(UpdateAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer


class BuildingDeleteAPIView(DestroyAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer