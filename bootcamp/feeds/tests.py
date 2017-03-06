from django.test import TestCase, Client
from django.contrib.auth.models import User

from .models import Feed


class FeedViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        user = User.objects.create_user(
            username='test_user',
            email='lennon@thebeatles.com',
            password='test_password'
        )
        self.feed = Feed.objects.create(user=user, post='test feed')

    def test_feeds(self):
        response = self.client.get('/feeds/')
        self.assertEqual(response.status_code, 200)

    def test_feed(self):
        response = self.client.get('/feeds/123/')
        self.assertEqual(response.status_code, 404)

        response = self.client.get(f'/feeds/{self.feed.pk}/')
        self.assertEqual(response.status_code, 200)
