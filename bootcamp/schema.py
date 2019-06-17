import graphene

from .feeds.schema import FeedQuery, CreateFeed, LikeFeed
from .authentication.schema import UserQuery, CreateToken


class Query(FeedQuery, UserQuery, graphene.ObjectType):
    node = graphene.Node.Field()


class Mutations(graphene.ObjectType):
    create_feed = CreateFeed.Field()
    like_feed = LikeFeed.Field()
    create_token = CreateToken.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)
