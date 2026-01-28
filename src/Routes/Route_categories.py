from flask import Blueprint
from src.Controller.Controller_categories import get_categories

categories_bp = Blueprint('categories', __name__)

@categories_bp.route('/categories', methods=['GET'])
def categories_route():
    return get_categories()
