import graphene

from graphene_django import DjangoObjectType

from .models import Tracks


class TracksType(DjangoObjectType):
    class Meta:
        model = Tracks


class Query(graphene.ObjectType):
    tracks = graphene.List(TracksType)

    def resolve_tracks(self, info):
        return Tracks.objects.all()
