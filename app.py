from src.Routes.Routes_projects import projects_bp
from src.Routes.Routes_customer_request import customer_request_bp
from flask import Flask
from flask_cors import CORS




app = Flask(__name__)

    

CORS(app,resources={r"/*": {"origins": [
    "http://localhost:5173"
    # DOMAIN
    
]}})

app.register_blueprint(projects_bp)
app.register_blueprint(customer_request_bp)

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000, debug=True)
