from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from src.Controller.Controller_customer_request import get_all_customer_requests, get_customer_requests_by_date, create_customer_request, update_request_status

customer_request_bp = Blueprint('customer_request', __name__)

@customer_request_bp.route('/customer_requests', methods=['GET'])
@jwt_required()
def customer_requests_route():
    return get_all_customer_requests()

@customer_request_bp.route('/customer_requests/by_date', methods=['GET'])
@jwt_required()
def customer_requests_by_date_route():
    from_date = request.args.get('from_date')
    return get_customer_requests_by_date(from_date)

@customer_request_bp.route('/customer_request', methods=['POST'])
def customer_request_route():
    return create_customer_request()

@customer_request_bp.route('/customer_requests/<id>/status', methods=['PUT'])
@jwt_required()
def update_customer_request_status_route(id):
    return update_request_status(id)