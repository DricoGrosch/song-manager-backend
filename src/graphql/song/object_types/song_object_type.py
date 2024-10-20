import graphene

class SongObjectType(graphene.ObjectType):
    id = graphene.Int()
    title = graphene.String()
    artist = graphene.String()
    difficulty = graphene.String()
    chords = graphene.String()

    def resolve_description(self):
        return f"{self.title} - {self.artist}"