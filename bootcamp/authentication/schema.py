from django.core import signing

import graphene
from graphql.error import GraphQLError
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

    def resolve_users(self, info, **kwargs):
        return User.objects.all().select_related('profile')


class AuthInput(graphene.InputObjectType):
    username = graphene.String(required=True)
    password = graphene.String(required=True)


class CreateToken(graphene.Mutation):
    class Arguments:
        auth = AuthInput(required=True)

    token = graphene.String(required=True)

    @staticmethod
    def mutate(root, info, auth):
        user = User.objects.filter(username=auth.username).first()
        if not user or not user.check_password(auth.password):
            raise GraphQLError('username or password is invalid.')

        return CreateToken(token=signing.dumps(user.id))
