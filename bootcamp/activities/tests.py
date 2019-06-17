from http import HTTPStatus

from django.test import TestCase, Client
from django.contrib.auth.models import User

from .models import Activity, Notification
from bootcamp.feeds.models import Feed


class NotificationMethodTests(TestCase):
    def setUp(self):
        from_user = User.objects.create_user(
            username='test_from_user',
            email='test@test.com',
            password='password'
        )
        to_user = User.objects.create_user(
            username='test_to_user',
            email='test_to@test.com',
            password='password'
        )
        feed = Feed.objects.create(user=from_user, post='test feed post')
        Activity.objects.create(user=to_user, activity_type=Activity.LIKE)

        self.notification = Notification.objects.create(
            notification_type=Notification.LIKED,
            from_user=from_user,
            to_user=to_user,
            feed=feed
        )

    def test_notification_str(self):
        str(self.notification)


class ActivitiesViewsTests(TestCase):
    def setUp(self):
        self.client = Client(HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        User.objects.create_user(
            username='test_user',
            email='lennon@thebeatles.com',
            password='test_password'
        )
        self.client.login(username='test_user', password='test_password')

    def test_notifications(self):
        response = self.client.get('/notifications/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_ajax_notifications(self):
        response = self.client.get('/notifications/last/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

        response = self.client.get('/notifications/check/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
