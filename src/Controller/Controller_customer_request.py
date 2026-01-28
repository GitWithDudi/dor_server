from src.Model.Model_customer_request import (fetch_all_customer_requests, fetch_customer_requests_by_date, add_new_customer_request, update_customer_request_status)
from datetime import date, datetime
from flask import request, jsonify
import validators



def get_all_customer_requests():
    try:
        requests = fetch_all_customer_requests()

        result = []
        for req in requests:
            result.append({
                "id": req["id"],
                "name": req["name"],
                "phone": req["phone"],
                "email": req["email"],
                "category": req["category"],
                "message": req["message"],
                "status": req["status"],
                "created_at": req["created_at"].isoformat() if req["created_at"] else None
            })
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def get_customer_requests_by_date(from_date):
    if from_date is None:
        return jsonify({"error": "from_date parameter is required"}), 400

    if isinstance(from_date, str):
        try:
            from_date = datetime.strptime(from_date, "%d-%m-%Y").date()
        except ValueError:
            return jsonify({"error": "from_date must be in DD-MM-YYYY format"}), 400
    elif not isinstance(from_date, date):
        return jsonify({"error": "from_date must be a string in DD-MM-YYYY format"}), 400

    if from_date > date.today():
        return jsonify({"error": "from_date cannot be in the future"}), 400

    try:
        requests = fetch_customer_requests_by_date(from_date)

        result = []
        for req in requests:
            result.append({
                "id": req["id"],
                "name": req["name"],
                "phone": req["phone"],
                "email": req["email"],
                "category": req["category"],
                "message": req["message"],
                "status": req["status"],
                "created_at": req["created_at"].isoformat() if req["created_at"] else None
            })
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def create_customer_request():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No data provided"}), 400

        name = data.get("name")
        phone = data.get("phone")
        email = data.get("email")
        message = data.get("message")
        category = data.get("category")

        if not name or not phone or not email or not message:
            return jsonify({"error": "Name, phone, email, and message are required fields"}), 400

        if not validators.email(email):
            return jsonify({"error": "Invalid email format"}), 400

        if not phone.isdigit() or len(phone) < 7:
            return jsonify({"error": "Invalid phone number format"}), 400

        try:
            new_request_id = add_new_customer_request(
                name=name,
                phone=phone,
                email=email,
                message=message,
                category=category
            )
            return jsonify({"message": "Customer request created successfully", "request_id": new_request_id}), 201
        except Exception as e:
            return jsonify({"error": f"Failed to create customer request: {str(e)}"}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500
