from flask import Blueprint, jsonify,request
from flask_jwt_extended import create_access_token
from src.utils import hash_password
from ...data import *

public_blueprint = Blueprint('public-blueprint',__name__)


@public_blueprint.route('/login', methods=['POST'])
def login():
    username = request.json.get("username")
    password = request.json.get("password")
    if username not in users or users[username] != hash_password(password):
        return jsonify({"msg": "Bad username or password"}), 401
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200
