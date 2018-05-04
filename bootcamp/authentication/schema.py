import graphene
import django_filters
from django.contrib.auth.models import User
from graphene.relay import Node
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from ..authentication.models import Profile


class UserObject(DjangoObjectType):
    class Meta:
        model = User
        interfaces = (Node,)


class ProfileObject(DjangoObjectType):
    class Meta:
        model = Profile


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = {
            'email': ['exact', 'istartswith']
        }

    @property
    def qs(self):
        return super().qs.select_related('profile')


class UserQuery(graphene.ObjectType):
    user = Node.Field(UserObject)
    profile = graphene.Field(ProfileObject)

    users = DjangoFilterConnectionField(UserObject, filterset_class=UserFilter)
