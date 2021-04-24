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


class CreateTracks(graphene.Mutation):

    track = graphene.Field(TracksType)

    class Arguments:
        title = graphene.String()
        description = graphene.String()
        url = graphene.String()

    def mutate(self, info, title, description, url):
        track = Tracks(title=title, description=description, url=url,)

        track.save()

        return CreateTracks(track=track)


class Mutation(graphene.ObjectType):
    create_tracks = CreateTracks.Field()
