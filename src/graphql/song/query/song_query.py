import graphene
from src.data import songs
from ..object_types.song_object_type import SongObjectType

class SongQuery(graphene.ObjectType):
    songs = graphene.List(
        SongObjectType,
        artist=graphene.String(),
        difficulty=graphene.String(),
        
    )
    song = graphene.Field(SongObjectType, id=graphene.Int(required=True))

    def resolve_song(self,info,id=None):
        return next((song for song in songs if song['id'] == id),None)

    def resolve_songs(self, info, artist=None, difficulty=None,id=None):
        filtered_songs = songs
        if artist:
            filtered_songs = [song for song in filtered_songs if song['artist'] == artist]
        if difficulty:
            filtered_songs = [song for song in filtered_songs if song['difficulty'] == difficulty]

        return filtered_songs