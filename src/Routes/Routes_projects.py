from flask import Blueprint
from flask_jwt_extended import jwt_required
from src.Controller.Controller__projects import get_projects, get_projects_by_category, create_project

projects_bp = Blueprint('projects', __name__)

@projects_bp.route('/projects', methods=['GET'])
def projects():
    return get_projects()

@projects_bp.route('/projects/<category>', methods=['GET'])
def projects_by_category(category):
    return get_projects_by_category(category)

@projects_bp.route('/projects', methods=['POST'])
@jwt_required()
def create_project_route():
    return create_project()