from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from department.factories import DepartmentFactory
from department.models import Department
from django.contrib.auth import get_user_model


User = get_user_model()

class DepartmentViewsetTestCase(TestCase):
    def setUp(self):
        self.department_object_1 = DepartmentFactory()

        self.manager = User.objects.create_user(username='manager', password='password123')
        self.department_object_2 = Department.objects.create(
            name='Initial Department',
            description='Initial Description',
            parent=None,
            manager=self.manager
        )
        self.url = reverse('department-detail', kwargs={'pk': self.department_object_2.pk})
        self.client = APIClient()

    def test_Department_list_should_success(self):
        url = '/department/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_Department_detail_should_success(self):
        url = '/department/1/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.department_object_1.name)
        self.assertContains(response, self.department_object_1.description)
        self.assertContains(response, self.department_object_1.manager)

    def test_Department_create_should_success(self):
        url = "/department/"
        form_data = {
            "name": "Отдел 228",
            "description": "Описание 228",
            "manager": 1
        }
        response = self.client.post(path=url, data=form_data)
        self.assertEqual(response.status_code, 201)

        query = Department.objects.filter(
            name=form_data["name"],
            description=form_data["description"],
            manager=form_data["manager"],
        ) 
        self.assertGreater(query.count(), 0)

    def test_Department_update_should_success(self):
        new_manager = User.objects.create_user(username='new_manager', password='password123')
        data = {
            'name': 'Updated Department',
            'description': 'Updated Description',
            'parent': None,
            'manager': new_manager.pk
        }
        response = self.client.put(self.url, data, format='json')
        self.assertEqual(response.status_code, 200)

        self.department_object_2.refresh_from_db()
        self.assertEqual(self.department_object_2.name, data['name'])
        self.assertEqual(self.department_object_2.description, data['description'])
        self.assertEqual(self.department_object_2.manager.pk, data['manager'])

    def test_Department_delete_should_success(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Department.objects.filter(pk=self.department_object_2.pk).exists())