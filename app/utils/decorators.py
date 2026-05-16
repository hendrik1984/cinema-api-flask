from functools import wraps
from flask_jwt_extended import get_jwt_identity
from app.models.user import User

def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        email = get_jwt_identity()
        user = User.query.filter_by(email=email).first()

        if not user or user.role != "admin":
            return {"error": "Admin access required"}, 403

        return fn(*args, **kwargs)

    return wrapper