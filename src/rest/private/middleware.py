
from .

@private_blueprint.before_request
def check_jwt_for_protected_routes():
    try:
        verify_jwt_in_request()  
    except NoAuthorizationError:
        return jsonify(message="Missing or invalid token"), 401
