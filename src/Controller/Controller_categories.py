from flask import jsonify
from src.Model.Model_categories import fetch_all_categories


def get_categories():
    try:
        categories = fetch_all_categories()

        result = []
        for category in categories:
            result.append({
                "id": category["id"],
                "category_name": category["category_name"]
            })
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
