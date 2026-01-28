from src.Routes.Routes_projects import projects_bp
from src.Routes.Routes_customer_request import customer_request_bp
from src.Routes.Route_login import login_bp
from src.Routes.Route_categories import categories_bp
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
jwt = JWTManager(app)

    

CORS(app,resources={r"/*": {"origins": [
    "http://localhost:5173"
    # DOMAIN
    
]}})

app.register_blueprint(projects_bp)
app.register_blueprint(customer_request_bp)
app.register_blueprint(login_bp)
app.register_blueprint(categories_bp)

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000, debug=True)
