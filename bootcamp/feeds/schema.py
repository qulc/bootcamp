import graphene
from graphene_django import DjangoObjectType

from .models import Feed


class FeedObject(DjangoObjectType):
    class Meta:
        model = Feed


class Query(graphene.ObjectType):
    feeds = graphene.List(FeedObject)

    def resolve_feeds(self, info):
        return Feed.objects.prefetch_related('feed_set').all()


schema = graphene.Schema(query=Query)
