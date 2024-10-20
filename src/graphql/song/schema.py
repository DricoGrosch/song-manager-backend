import graphene

from src.graphql.song.mutations.create_song_mutation import CreateSongMutation
from src.graphql.song.mutations.delete_song_mutation import DeleteSongMutation
from src.graphql.song.mutations.update_song_mutation import UpdateSongMutation
from src.graphql.song.query.song_query import SongQuery


class SongMutations(graphene.ObjectType):
    create_song = CreateSongMutation.Field()
    update_song = UpdateSongMutation.Field()
    delete_song = DeleteSongMutation.Field()


song_schema = graphene.Schema(query=SongQuery, mutation=SongMutations)