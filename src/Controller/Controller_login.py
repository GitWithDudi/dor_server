from flask import jsonify
from flask_jwt_extended import create_access_token
from dotenv import load_dotenv
load_dotenv()
import os


def login_controller(request):
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    admin_user = os.getenv('ADMIN_USERNAME')
    admin_pass = os.getenv('ADMIN_PASSWORD')

    if username == admin_user and password == admin_pass:
        access_token = create_access_token(identity=username)
        return jsonify({"access_token": access_token}), 200
    else:
        return jsonify({"msg": "Invalid username or password"}), 401
