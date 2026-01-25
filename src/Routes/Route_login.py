from flask import Blueprint, request
from src.Controller.Controller_login import login_controller

login_bp = Blueprint('login_routes', __name__)

@login_bp.route('/login', methods=['POST'])
def login_route():
    return login_controller(request)
