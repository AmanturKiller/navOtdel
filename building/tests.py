from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()
class AdminPageTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username='admin', password='password'
        )

    def test_admin_page_status(self):
        self.client.login(username='admin', password='password')
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200, "Страница администратора не вернула статус 200")