import graphene
from src.data import songs

class DeleteSongMutation(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)  # Song ID to delete

    success = graphene.Boolean()

    def mutate(self, info, id):
        # Find the song by ID
        song_to_delete = next((song for song in songs if song['id'] == id), None)
        if song_to_delete is None:
            raise Exception("Song not found")
        # prevent deleted just for test purpose
        # songs.remove(song_to_delete)
        return DeleteSongMutation(success=True)
