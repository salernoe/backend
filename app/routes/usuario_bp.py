from flask import Blueprint

from ..controllers.usuario_controller import UsuarioController

usuario_bp = Blueprint('usuario_bp', __name__)

usuario_bp.route('/get_all', methods=['GET'])(UsuarioController.get_all)
usuario_bp.route('/get_one/<int:id_usuario>', methods=['GET'])(UsuarioController.get)
usuario_bp.route('/post', methods=['POST'])(UsuarioController.create)
usuario_bp.route('/put/<int:id_usuario>', methods=['PUT'])(UsuarioController.update)
usuario_bp.route('/delete/<int:id_usuario>', methods=['DELETE'])(UsuarioController.delete)