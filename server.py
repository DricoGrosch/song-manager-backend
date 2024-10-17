from datetime import timedelta
from flask import Flask, jsonify, request
from flask_cors import CORS
import hashlib
from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, verify_jwt_in_request
from flask_jwt_extended.exceptions import NoAuthorizationError

def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

users = {
    "admin": hash_password("123")
}

app = Flask(__name__)
CORS(app)
app.config['JWT_SECRET_KEY'] = 'secret-key'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)
jwt = JWTManager(app)

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
@app.before_request
def check_jwt_for_protected_routes():
    print(request.path)
    print(request.path)
    print(request.path)
    print(request.path == '/login')
    if request.path == '/login':
        return 
    try:
        verify_jwt_in_request()  
    except NoAuthorizationError:
        return jsonify(message="Missing or invalid token"), 401
# Rotas para gerenciamento de músicas
@app.route('/', methods=['GET'])
def home():
    return 'home page'
# Rotas para gerenciamento de músicas
@app.route('/songs', methods=['GET'])
def get_songs():
    return jsonify(songs)

@app.route('/songs', methods=['POST'])
def add_song():
    new_song = request.json
    new_song['id'] = len(songs) + 1
    songs.append(new_song)
    return jsonify(new_song), 201


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    # Verificar se o usuário existe e se a senha está correta
    if username not in users or users[username] != hash_password(password):
        return jsonify({"msg": "Bad username or password"}), 401

    # Gerar token JWT para o usuário autenticado
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200

