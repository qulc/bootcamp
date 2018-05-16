import graphene
from graphene_django import DjangoObjectType
from graphene_django.fields import DjangoConnectionField

from .models import Feed


class FeedObject(DjangoObjectType):
    class Meta:
        model = Feed
        interfaces = [graphene.Node]


class FeedQuery(graphene.ObjectType):
    feed = graphene.Node.Field(FeedObject)
    feeds = DjangoConnectionField(FeedObject, first=graphene.Int(default_value=5))

    def resolve_feeds(self, info, **kwargs):
        return Feed.objects.select_related(
            'user', 'user__profile'
        ).prefetch_related('feed_set').filter(parent=None)
