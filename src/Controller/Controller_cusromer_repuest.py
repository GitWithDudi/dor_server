from src.Model.Model_customer_request import (fetch_all_customer_requests, fetch_customer_requests_by_date, add_new_customer_request)
from datetime import date, datetime


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
