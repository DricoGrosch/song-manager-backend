import graphene
from src.data import songs

class UpdateSongMutation(graphene.Mutation):
    id = graphene.Int()
    title = graphene.String()
    artist = graphene.String()
    difficulty = graphene.String()
    chords = graphene.String()

    class Arguments:
        id = graphene.Int(required=True)
        title = graphene.String()
        artist = graphene.String()
        difficulty = graphene.String()
        chords = graphene.String()

    def mutate(self, info, id, title=None, artist=None, difficulty=None, chords=None):
        song = next((s for s in songs if s['id'] == id), None)
        if song is None:
            raise Exception("Song not found")

        # Update the song's attributes if provided
        if title:
            song['title'] = title
        if artist:
            song['artist'] = artist
        if difficulty:
            song['difficulty'] = difficulty
        if chords:
            song['chords'] = chords

        return UpdateSongMutation(
            id=song['id'],
            title=song['title'],
            artist=song['artist'],
            difficulty=song['difficulty'],
            chords=song['chords']
        )
