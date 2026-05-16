from app.models.user import User
from app.extensions import db
from flask_jwt_extended import create_access_token
from datetime import datetime, timezone

class UserService:

    @staticmethod
    def register_user(email, username, password):
        if User.query.filter_by(email=email).first():
            raise ValueError("Email already exists")

        if User.query.filter_by(username=username).first():
            raise ValueError("Username already exists")

        user = User(email=email, username=username)
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        return user

    @staticmethod
    def login_user(email, password):
        user = User.query.filter_by(email=email).first()

        if not user or not user.check_password(password):
            raise ValueError("Invalid credentials")

        token = create_access_token(identity=user.email)
        return token

    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def get_user_by_id(user_id):
        user = User.query.get(user_id)

        if not user:
            raise ValueError("User not found")

        return user

    @staticmethod
    def update_user(user_id, email=None, username=None, password=None, role=None):
        user = User.query.get(user_id)

        if not user:
            raise ValueError("User not found")

        if email:
            user.email = email

        if username:
            existing = User.query.filter_by(username=username).first()
            if existing and existing.id != user.id:
                raise ValueError("Username already in use")
            user.username = username

        if password:
            user.set_password(password)

        if role:
            user.role = role

        user.updated_at = datetime.now(timezone.utc)

        db.session.commit()

        return user

    @staticmethod
    def delete_user(user_id):
        user = User.query.get(user_id)

        if not user:
            raise ValueError("User not found")

        db.session.delete(user)
        db.session.commit()

        return True