from django.test import TestCase
from django.contrib.auth.models import User


class ProfileMethodTests(TestCase):
    def setUp(self):
        user = User.objects.create_user(
            username='lichun',
            email='i@lichun.me',
            password='lichun_password',
        )
        user.profile.url = 'https://lichun.me/'
        user.save()

    def test_get_profile(self):
        user = User.objects.get(username='lichun')

        url = user.profile.get_url()
        self.assertEqual(url, 'https://lichun.me/')

        picture_url = user.profile.get_picture()
        self.assertEqual(picture_url, '/static/img/user.png')

        screen_name = user.profile.get_screen_name()
        self.assertEqual(screen_name, 'lichun')
