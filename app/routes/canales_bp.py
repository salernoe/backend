from ..controllers.canales_controllers import CanalController  
from flask import Blueprint

canal_bp = Blueprint('canal_bp', __name__)

canal_bp.route('/get_all', methods=['GET'])(CanalController.get_all)
canal_bp.route('/get_one/<int:id_canal>', methods=['GET'])(CanalController.get)
canal_bp.route('/post', methods=['POST'])(CanalController.create)
canal_bp.route('/put/<int:id_canal>', methods=['PUT'])(CanalController.update)
canal_bp.route('/delete/<int:id_canal>', methods=['DELETE'])(CanalController.delete)