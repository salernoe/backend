from flask import Blueprint

from ..controllers.chats_controllers import ChatController  

chat_bp = Blueprint('chat_bp', __name__)

chat_bp.route('/get_all', methods=['GET'])(ChatController.get_all)
chat_bp.route('/get_one/<int:id_mensaje>', methods=['GET'])(ChatController.get)
chat_bp.route('/post', methods=['POST'])(ChatController.create)
chat_bp.route('/put/<int:id_mensaje>', methods=['PUT'])(ChatController.update)
chat_bp.route('/delete/<int:id_mensaje>', methods=['DELETE'])(ChatController.delete)