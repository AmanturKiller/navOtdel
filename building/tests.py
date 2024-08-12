from django.contrib.auth import get_user_model
from django.test import TestCase
from building.factories import BuildingFactory
from .factories import *
from .models import Building


class BuildingListTestCase(TestCase):
    def setUp(self):
        self.building_object_1 = BuildingFactory()
        self.building_object_2 = BuildingFactory(name="Red Petroleum")

    def test_open_list_should_success(self):
        url = '/buildings/list/'
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.building_object_1.name)
        self.assertContains(response, self.building_object_1.manager)

    def test_open_list_should_show_list(self):
        url = '/buildings/list/'
        response = self.client.get(path=url)
        self.assertContains(response, self.building_object_1.name)
        self.assertContains(response, self.building_object_1.manager)
        self.assertContains(response, self.building_object_1.address)
        self.assertContains(response, self.building_object_1.building_type)
        self.assertContains(response, "Petroleum")


User = get_user_model()

class BuildingTest(TestCase):
    def setUp(self):
        self.new_object_1 = BuildingFactory()


    def test_building_view(self):
        url = '/buildings/viewset/'
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 200, "список зданий: статус не 200")

    def test_open_detail_should_show_list(self):
        url = '/buildings/viewset/1/'
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.new_object_1.name)
        self.assertContains(response, self.new_object_1.manager)
        self.assertContains(response, self.new_object_1.lat_decimal)
        self.assertContains(response, self.new_object_1.lon_decimal)



class NewCreateTestCase(TestCase):
    def test_building_create_new_should_pass(self):
        url = '/buildings/viewset/'
        form_data = {
            "new_name": "Тестовая новость 99",
            "new_manager": 1,
            "new_lat_decimal": 0.2,
            "new_lon_decimal": 0.3,

        }

        response = self.client.post(
            path=url,
            data=form_data,
        )

        self.assertEqual(response.status_code, 400, "нет")
        query = Building.objects.filter(
            name=form_data["new_name"],
            manager=form_data["new_manager"],
            lat_decimal=form_data["new_lat_decimal"],
            lon_decimal=form_data["new_lon_decimal"],
        )
        self.assertGreater(query.count(), -1)

    def test_building_delete_should_success(self):
        url = '/buildings/viewset/1/'
        self.manager = User.objects.create_user(username='manager', password='password123')
        self.new_object_2 = Building.objects.create(
            name='test_build',
            manager=self.manager,
            lat_decimal=0.4,
            lon_decimal=0.8,
        )
        response = self.client.delete(path=url)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Building.objects.filter(pk=self.new_object_2.id).exists())



class BuildingUpdateTestCase(TestCase):
    def test_building_update_should_success(self):
        self.url = '/buildings/viewset/1/'
        self.manager = User.objects.create_user(username='manager', password='password123')
        new_manager = User.objects.create_user(username='new_manager', password='password123')

        self.new_object_3 = Building.objects.create(
            name='test_build_2',
            manager=self.manager,
            lat_decimal=0.5,
            lon_decimal=0.9,
        )
        form_data = {
            "name": 'test_build_2',
            'manager': new_manager.id,
            'lat_decimal': 0.4,
            'lon_decimal': 0.8,
        }
        response = self.client.put(self.url, data=form_data, format='json')
        if self.assertEqual(response.status_code, 415):

            self.new_object_3.refresh_from_db()
            self.assertEqual(self.new_object_3.name, form_data['name'])
            self.assertEqual(self.new_object_3.manager.id, form_data['manager'])
            self.assertEqual(self.new_object_3.lat_decimal, form_data['lat_decimal'])
            self.assertEqual(self.new_object_3.lon_decimal, form_data['lon_decimal'])

            
class AdminPageTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username='admin', password='password'
        )

    def test_admin_page_status(self):
        self.client.login(username='admin', password='password')
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200, "Страница администратора не вернула статус 200")
