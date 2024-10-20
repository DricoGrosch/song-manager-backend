

from src.utils import hash_password


songs = [
    {'id': 1, 'title': 'Sweet Child O\' Mine', 'artist': 'Guns N\' Roses', 'difficulty': 'Medium', 'chords': 'G D A'},
    {'id': 2, 'title': 'Stairway to Heaven', 'artist': 'Led Zeppelin', 'difficulty': 'Hard', 'chords': 'Am G F'},
]

playlists = [
    {'id': 1, 'name': 'Rock Classics', 'songs': [1, 2]},  # Referências aos IDs das músicas
]

techniques = [
    {'id': 1, 'name': 'Palm Muting', 'description': 'Técnica para abafar as cordas com a mão.'},
    {'id': 2, 'name': 'Bending', 'description': 'Técnica de puxar a corda para alterar o tom da nota.'},
]

progress = [
    {'id': 1, 'song_id': 1, 'progress': '50%'},  # Progresso da prática de uma música
]

users = {
    "admin": hash_password("123")
}
