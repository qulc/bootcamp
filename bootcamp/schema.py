import graphene

from .feeds.schema import FeedQuery
from .authentication.schema import UserQuery


class Query(FeedQuery, UserQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
