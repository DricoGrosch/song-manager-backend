from flask import Blueprint, jsonify,request
from flask_jwt_extended import  verify_jwt_in_request
from flask_jwt_extended.exceptions import NoAuthorizationError
from ...data import *

private_blueprint = Blueprint('private-blueprint',__name__)


@private_blueprint.before_request
def check_jwt_for_protected_routes():
    try:
        verify_jwt_in_request()  
    except NoAuthorizationError:
        return jsonify(message="Missing or invalid token"), 401

@private_blueprint.route('/', methods=['GET'])
def home():
    return 'home page'

@private_blueprint.route('/songs', methods=['GET'])
def get_songs():
    return jsonify(songs)

@private_blueprint.route('/songs', methods=['POST'])
def add_song():
    new_song = request.json
    new_song['id'] = len(songs) + 1
    songs.append(new_song)
    return jsonify(new_song), 201
