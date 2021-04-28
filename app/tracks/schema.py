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
        user = info.context.user

        if user.is_anonymous:
            raise Exception('Log in to add track')

        track = Tracks(title=title, description=description,
                       url=url, posted_by=user)

        track.save()

        return CreateTracks(track=track)


class Mutation(graphene.ObjectType):
    create_tracks = CreateTracks.Field()
