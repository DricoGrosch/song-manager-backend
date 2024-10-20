from unittest import TestCase
from src.graphql.song.schema import song_schema
from src.data import songs

class TestGraphQLQueries(TestCase):

    def test_get_songs(self):
        query = '''
        query {
            songs {
                id
                title
                artist
                difficulty
                chords
            }
        }
        '''
        result = song_schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['songs']), len(songs))

    # Test case for adding a new song
    def test_add_song(self):
        mutation = '''
        mutation {
            createSong(title: "Test Song", artist: "Test Artist", difficulty: "Easy", chords: "C D G") {
                id
                title
                artist
                difficulty  
                chords
            }
        }
        '''
        result = song_schema.execute(mutation)
        self.assertIsNone(result.errors)
        self.assertEqual(result.data['createSong']['title'], "Test Song")

    def test_get_songs_by_artist(self):
        query = '''
        query {
            songs(artist: "Test Artist") {
                id
                title
                artist
                difficulty
                chords
            }
        }
        '''
        result = song_schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertGreaterEqual(len(result.data['songs']), 1)
        for song in result.data['songs']:
            self.assertEqual(song['artist'], "Test Artist")

    # Test case for retrieving a song by ID
    def test_get_song_by_id(self):
        query = '''
        query {
            song(id: 1) {
                id
                title
                artist
                difficulty
                chords
            }
        }
        '''
        result = song_schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(result.data['song']['id'], 1)
        self.assertEqual(result.data['song']['title'], songs[0]['title'])

    # Test case for adding a song with missing fields
    def test_add_song_with_missing_fields(self):
        mutation = '''
        mutation {
            createSong(title: "Incomplete Song", artist: "Test Artist", difficulty: "Medium") {
                id
                title
                artist
                difficulty
                chords
            }
        }
        '''
        result = song_schema.execute(mutation)
        self.assertIsNotNone(result.errors)
        self.assertIn('''Field "createSong" argument "chords" of type "String!" is required but not provided.''', str(result.errors))

    # Test case for adding a song with invalid data
    def test_add_song_with_empty_title(self):
        mutation = '''
        mutation {
            createSong(title: "", artist: "Test Artist", difficulty: "Easy", chords: "C D G") {
                id
                title
                artist
                difficulty
                chords
            }
        }
        '''
        result = song_schema.execute(mutation)
        self.assertIsNotNone(result.errors)  # Expecting an error due to empty title
        self.assertIn("title: String! (must not be empty)", str(result.errors))
    
    def test_add_song_with_null_title(self):
        mutation = '''
        mutation {
            createSong(artist: "Test Artist", difficulty: "Easy", chords: "C D G") {
                id
                title
                artist
                difficulty
                chords
            }
        }
        '''
        result = song_schema.execute(mutation)
        self.assertIsNotNone(result.errors)  # Expecting an error due to empty title
        self.assertIn('''Field "createSong" argument "title" of type "String!" is required but not provided.''', str(result.errors))

    # Test case for updating a song (assuming an updateSong mutation exists)
    def test_update_song(self):
        mutation = '''
        mutation {
            updateSong(id: 1, title: "Updated Song Title") {
                id
                title
                artist
                difficulty
                chords
            }
        }
        '''
        result = song_schema.execute(mutation)
        self.assertIsNone(result.errors)
        self.assertEqual(result.data['updateSong']['title'], "Updated Song Title")


    # Test case for deleting a song (assuming a deleteSong mutation exists)
    def test_delete_song(self):
        mutation = '''
        mutation {
            deleteSong(id: 1) {
                success
            }
        }
        '''
        result = song_schema.execute(mutation)
        self.assertIsNone(result.errors)
        self.assertTrue(result.data['deleteSong']['success'])
