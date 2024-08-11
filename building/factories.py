import factory
from building.models import Building
from django.contrib.auth import get_user_model


User = get_user_model()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'user{n}')


class BuildingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Building

    name = factory.Sequence(lambda n: f'test name {n}')
    manager = factory.SubFactory(UserFactory)
    address = factory.Sequence(lambda n: f'test address {n}')
    lat_decimal = factory.Sequence(lambda n: f'{n}')
    lon_decimal = factory.Sequence(lambda n: f'{n}')
    building_type = Building.OFFICE