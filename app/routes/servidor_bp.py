from flask import Blueprint

from ..controllers.servidores_controllers import ServidorController

servidor_bp = Blueprint('servidor_bp', __name__)

servidor_bp.route('/get_all', methods=['GET'])(ServidorController.get_all)
servidor_bp.route('/get_one/<int:id_servidor>', methods=['GET'])(ServidorController.get)
servidor_bp.route('/post', methods=['POST'])(ServidorController.create)
servidor_bp.route('/put/<int:Id_servidor>', methods=['PUT'])(ServidorController.update)
servidor_bp.route('/delete/<int:Id_servidor>', methods=['DELETE'])(ServidorController.delete)