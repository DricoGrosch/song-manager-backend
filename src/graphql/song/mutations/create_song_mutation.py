import graphene
from src.data import songs

class CreateSongMutation(graphene.Mutation):
    id = graphene.Int()
    title = graphene.String()
    artist = graphene.String()
    difficulty = graphene.String()
    chords = graphene.String()

    class Arguments:
        title = graphene.String(required=True)
        artist = graphene.String(required=True)
        difficulty = graphene.String(required=True)
        chords = graphene.String(required=True)

    def mutate(self, info, title, artist, difficulty, chords):
        if not title.strip():   
            raise Exception("title: String! (must not be empty)")
        
        new_song = {
            'id': len(songs) + 1,
            'title': title,
            'artist': artist,
            'difficulty': difficulty,
            'chords': chords
        }
        songs.append(new_song)
        return CreateSongMutation(
            id=new_song['id'],
            title=new_song['title'],
            artist=new_song['artist'],
            difficulty=new_song['difficulty'],
            chords=new_song['chords']
        )
