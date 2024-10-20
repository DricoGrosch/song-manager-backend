import graphene

from ..data import songs
from .object_type import Song

class SongQuery(graphene.ObjectType):
    songs = graphene.List(Song)

    def resolve_songs(self, info):
        return songs