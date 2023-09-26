from flask import Blueprint

from ..controllers.usuario_controller import UsuarioController

login_bp = Blueprint('login_bp', __name__)

login_bp.route('/get_all', methods=['GET'])(UsuarioController.get_all)
login_bp.route('/get_one/<int:id_usuario>', methods=['GET'])(UsuarioController.get)
login_bp.route('/post', methods=['POST'])(UsuarioController.create)
login_bp.route('/put/<int:id_usuario>', methods=['PUT'])(UsuarioController.update)
login_bp.route('/delete/<int:id_usuario>', methods=['DELETE'])(UsuarioController.delete)