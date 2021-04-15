import graphene

from app.tracks import schema


class Query(schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
