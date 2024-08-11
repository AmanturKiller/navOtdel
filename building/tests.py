from django.test import TestCase
from building.factories import BuildingFactory

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
