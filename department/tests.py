from django.test import TestCase

class DepartmentListTestCase(TestCase):
    def test_department_list_status(self):
        url = '/department/list/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200, "Страница со списком отделов не вернула статус 200")