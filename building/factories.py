import factory
from .models import Building
from django.contrib.auth import get_user_model

User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    id = 1


class BuildingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Building

    name = factory.Sequence(lambda n: f'test new {n}')
    manager = factory.SubFactory(UserFactory)
    lat_decimal = 0.1
    lon_decimal = 0.2