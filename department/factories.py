import factory
from department.models import Department
from django.contrib.auth import get_user_model


User = get_user_model()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    username = factory.Sequence(lambda n: f'{n}')


class DepartmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Department
        
    name = factory.Sequence(lambda n: f'test name {n}')
    description = factory.Sequence(lambda n: f'test description {n}')
    manager = factory.SubFactory(UserFactory)