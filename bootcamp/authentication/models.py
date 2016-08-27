from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from bootcamp.activities.models import Notification


class Profile(models.Model):
    user = models.OneToOneField(User)
    url = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    job_title = models.CharField(max_length=50, null=True, blank=True)
    picture_url = models.CharField(max_length=120, null=True, blank=True)

    def get_url(self):
        url = self.url
        if not self.url.startswith("http://") \
                and not self.url.startswith("https://") \
                and len(self.url) > 0:
            url = "http://" + str(self.url)
        return url

    def get_picture(self):
        if not self.picture_url:
            no_picture = '/static/img/user.png'
            return no_picture

        return self.picture_url

    def get_screen_name(self):
        if self.user.get_full_name():
            return self.user.get_full_name()

        return self.user.username

    def notify_liked(self, feed):
        if self.user != feed.user:
            Notification.objects.create(
                notification_type=Notification.LIKED,
                from_user=self.user,
                to_user=feed.user,
                feed=feed
            )

    def unotify_liked(self, feed):
        if self.user != feed.user:
            Notification.objects.filter(
                notification_type=Notification.LIKED,
                from_user=self.user,
                to_user=feed.user,
                feed=feed
            ).delete()

    def notify_commented(self, feed):
        if self.user != feed.user:
            Notification(
                notification_type=Notification.COMMENTED,
                from_user=self.user,
                to_user=feed.user,
                feed=feed
            ).save()

    def notify_also_commented(self, feed):
        comments = feed.get_comments()
        users = set()

        for comment in comments:
            if comment.user != self.user and comment.user != feed.user:
                users.add(comment.user.pk)

        for user in users:
            Notification(
                notification_type=Notification.ALSO_COMMENTED,
                from_user=self.user,
                to_user=User(id=user),
                feed=feed
            ).save()

    def notify_favorited(self, question):
        if self.user != question.user:
            Notification(
                notification_type=Notification.FAVORITED,
                from_user=self.user,
                to_user=question.user,
                question=question
            ).save()

    def unotify_favorited(self, question):
        if self.user != question.user:
            Notification.objects.filter(
                notification_type=Notification.FAVORITED,
                from_user=self.user,
                to_user=question.user,
                question=question
            ).delete()

    def notify_answered(self, question):
        if self.user != question.user:
            Notification.objects.create(
                notification_type=Notification.ANSWERED,
                from_user=self.user,
                to_user=question.user,
                question=question
            )

    def notify_accepted(self, answer):
        if self.user != answer.user:
            Notification.objects.create(
                notification_type=Notification.ACCEPTED_ANSWER,
                from_user=self.user,
                to_user=answer.user,
                answer=answer
            )

    def unotify_accepted(self, answer):
        if self.user != answer.user:
            Notification.objects.filter(
                notification_type=Notification.ACCEPTED_ANSWER,
                from_user=self.user,
                to_user=answer.user,
                answer=answer
            ).delete()


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
