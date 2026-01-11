from flask import jsonify, request
import validators
import os
from src.Model.Model_projects import fetch_all_projects, fetch_project_by_category_id, add_new_project


def get_projects():
    projects = fetch_all_projects()
    
    result = []
    for project in projects:
        result.append({
            "id": project["id"],
            "project_name": project["project_name"],
            "description": project["description"],
            "image": project["image"],
            "category_name": project["category_name"]
        })
    return jsonify(result), 200



def get_projects_by_category(category_id: int):
    projects = fetch_project_by_category_id(category_id)
    
    result = []
    for project in projects:
        result.append({
            "id": project["id"],
            "project_name": project["project_name"],
            "description": project["description"],
            "image": project["image"],
            "category_name": project["category_name"]
        })
    
    return jsonify(result), 200



def create_project():
    data = request.get_json()

    project_name: str = data.get("project_name")
    description: str = data.get("description")
    image: str = data.get("image")
    category_id: int = data.get("category_id")

    if not all([project_name, description, category_id]):
        return jsonify({"error": "Missing required fields"}), 400
    
    if image and not (
        validators.url(image)
        or os.path.isabs(image)
        ):
        return jsonify({"error": "Invalid image"}), 400
    
    try:
        category_id = int(category_id)
    except (TypeError, ValueError):
        return jsonify({"error": "category_id must be an integer"}), 400
    
    
    try:
        new_project_id = add_new_project(
            project_name=project_name,
            description=description,
            image=image,
            category_id=category_id
            )
        return jsonify({"message": "Project created", "project_id": new_project_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    
