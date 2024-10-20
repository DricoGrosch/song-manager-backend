from datetime import timedelta
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask import Flask, jsonify, request
from flask_graphql import GraphQLView
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, verify_jwt_in_request
import graphene

from src.song.mutation import SongMutation
from src.song.query import SongQuery


from .rest.public.routes import public_blueprint
from .rest.private.routes import private_blueprint
from .data import *


app = Flask(__name__)
CORS(app)
app.config['JWT_SECRET_KEY'] = 'secret-key'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)
JWTManager(app)

app.register_blueprint(public_blueprint)
app.register_blueprint(private_blueprint)

app.add_url_rule(
    '/graphql-users',
    view_func=GraphQLView.as_view('graphql-users', schema= graphene.Schema(query=SongQuery, mutation=SongMutation), graphiql=True)
)