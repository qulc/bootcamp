import graphene
import django_filters
from graphene.relay import Node
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Feed


class FeedObject(DjangoObjectType):
    class Meta:
        model = Feed
        interfaces = (Node,)


class FeedFilter(django_filters.FilterSet):
    class Meta:
        model = Feed
        fields = ['date']

    @property
    def qs(self):
        return super().qs.select_related(
            'user', 'user__profile'
        ).prefetch_related('feed_set').filter(parent=None)


class FeedQuery(graphene.ObjectType):
    feed = Node.Field(FeedObject)
    feeds = DjangoFilterConnectionField(FeedObject, filterset_class=FeedFilter)
