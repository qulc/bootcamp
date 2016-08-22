from django.test import TestCase, Client
from django.contrib.auth.models import User


class CoreViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create_user(
            username='test_user',
            email='lennon@thebeatles.com',
            password='johnpassword'
        )

    def test_home_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_network_url(self):
        response = self.client.get('/network/')
        self.assertEqual(response.status_code, 200)

    def test_profile_url(self):
        response = self.client.get('/test_user/')
        self.assertEqual(response.status_code, 200)
