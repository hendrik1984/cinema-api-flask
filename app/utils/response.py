from flask import jsonify

def api_response(data=None, error="", message="", status_code=200, meta=None):
    return jsonify(
        {
            "data": data,
            "error": error,
            "message": message,
            "meta": meta or {},
        }
    ), status_code