from http import HTTPStatus

from django.test import TestCase, Client
from django.contrib.auth.models import User


class CoreViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create_user(
            username='test_user',
            email='lennon@thebeatles.com',
            password='test_password'
        )
        self.client.login(username='test_user', password='test_password')

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_network(self):
        response = self.client.get('/network/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_profile(self):
        response = self.client.get('/test_user/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_settings(self):
        response = self.client.get('/settings/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_picture(self):
        response = self.client.get('/settings/picture/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_password(self):
        response = self.client.get('/settings/password/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
