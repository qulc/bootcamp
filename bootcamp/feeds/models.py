import bleach

from django.db import models
from django.utils.html import escape
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from bootcamp.activities.models import Activity


class Feed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    post = models.TextField(max_length=255)
    parent = models.ForeignKey('Feed', null=True, blank=True, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)

    class Meta:
        verbose_name = _('Feed')
        verbose_name_plural = _('Feeds')
        ordering = ('-date',)

    def __str__(self):
        return self.post

    @staticmethod
    def get_feeds(from_feed=None):
        if from_feed is not None:
            feeds = Feed.objects.filter(parent=None, id__lte=from_feed)
        else:
            feeds = Feed.objects.filter(parent=None)
        return feeds.prefetch_related('user__profile')

    @staticmethod
    def get_feeds_after(feed):
        feeds = Feed.objects.filter(parent=None, id__gt=feed)
        return feeds

    def get_comments(self):
        return Feed.objects.filter(parent=self).order_by('date')

    def calculate_likes(self):
        likes = Activity.objects.filter(activity_type=Activity.LIKE,
                                        feed=self.pk).count()
        self.likes = likes
        self.save()
        return self.likes

    def get_likes(self):
        likes = Activity.objects.filter(activity_type=Activity.LIKE,
                                        feed=self.pk)
        return likes

    def get_likers(self):
        likes = self.get_likes()
        likers = []
        for like in likes:
            likers.append(like.user)
        return likers

    def calculate_comments(self):
        self.comments = Feed.objects.filter(parent=self).count()
        self.save()
        return self.comments

    def comment(self, user, post):
        feed_comment = Feed(user=user, post=post, parent=self)
        feed_comment.save()
        self.comments = Feed.objects.filter(parent=self).count()
        self.save()
        return feed_comment

    def linkfy_post(self):
        return bleach.linkify(escape(self.post))

    @classmethod
    def like(cls, feed_id, user):
        feed = Feed.objects.get(pk=feed_id)
        like = Activity.objects.filter(
            activity_type=Activity.LIKE, feed=feed_id, user=user)

        if like:
            user.profile.unotify_liked(feed)
            like.delete()
        else:
            Activity.objects.create(
                feed=feed_id,
                user=user,
                activity_type=Activity.LIKE
            )
            user.profile.notify_liked(feed)

        feed.calculate_likes()
        return feed
