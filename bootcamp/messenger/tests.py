from django.test import TestCase, Client
from django.contrib.auth.models import User


class MessengerViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create_user(
            username='test_user',
            email='lennon@thebeatles.com',
            password='test_password'
        )
        User.objects.create_user(
            username='test_user_1',
            email='lennon_1@thebeatles.com',
            password='test_password'
        )
        self.client.login(username='test_user', password='test_password')

    def test_inbox(self):
        response = self.client.get('/messages/')
        self.assertEqual(response.status_code, 200)

    def test_messages(self):
        response = self.client.get('/messages/no_user/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/messages/test_user/')
        self.assertEqual(response.status_code, 200)

    def test_new_message(self):
        response = self.client.get('/messages/new/')
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/messages/new/', {
            'to': 'test_user_1',
            'message': 'test message'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/messages/test_user_1/')
