from src.Model.Model_customer_request import (fetch_all_customer_requests, fetch_customer_requests_by_date, add_new_customer_request)
from datetime import date, datetime
from flask import Request, jsonify
import validators



def get_all_customer_requests(token):
    if not token:
        raise PermissionError("Missing authentication token")

    requests = fetch_all_customer_requests(token)
    return requests


def get_customer_requests_by_date(token, from_date):
    if not token:
        raise PermissionError("Missing authentication token")

    if from_date is None:
        raise ValueError("from_date parameter is required")

    if isinstance(from_date, str):
        try:
            from_date = datetime.strptime(from_date, "%d-%m-%Y").date()
        except ValueError:
            raise ValueError("from_date must be in DD-MM-YYYY format")
    elif not isinstance(from_date, date):
        raise TypeError("from_date must be a string in DD-MM-YYYY format")

    if from_date > date.today():
        raise ValueError("from_date cannot be in the future")

    return fetch_customer_requests_by_date(token, from_date)


def create_customer_request():
    data = Request.get_json()
    
    name = data.get("name")
    phone = data.get("phone")
    email = data.get("email")
    message = data.get("message")
    category = data.get("category")

    if not name or not phone or not email or not message:
        raise ValueError("Name, phone, email, and message are required fields")
    if not validators.email(email):
        raise ValueError("Invalid email format")
    if not phone.isdigit() or len(phone) < 7:
        raise ValueError("Invalid phone number format")

    try:
        add_new_customer_request(
            name=name,
            phone=phone,
            email=email,
            message=message,
            category=category
        )
    except Exception as e:
        raise RuntimeError(f"Failed to create customer request: {e}")           
    return jsonify({"message": "Customer request created successfully"}), 201
    