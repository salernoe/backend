from flask import Blueprint
from ..models.exeptions import UsuarioNotFound
errors = Blueprint("errors", __name__)

@errors.app_errorhandler(UsuarioNotFound)
def handle_bad_request(error):
    return error.get_response()