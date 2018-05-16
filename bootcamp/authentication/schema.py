import graphene
from django.contrib.auth.models import User
from graphene_django import DjangoObjectType, DjangoConnectionField

from ..authentication.models import Profile


class UserObject(DjangoObjectType):
    class Meta:
        model = User
        interfaces = (graphene.Node,)


class ProfileObject(DjangoObjectType):
    class Meta:
        model = Profile


class UserQuery(graphene.ObjectType):
    profile = graphene.Field(ProfileObject)

    user = graphene.Node.Field(UserObject)
    users = DjangoConnectionField(UserObject)

    def resolve_users(self):
        return User.objects.all().select_related('profile')
