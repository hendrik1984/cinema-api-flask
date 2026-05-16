from app.extensions import db
from app.models.base import BaseModel
from werkzeug.security import generate_password_hash, check_password_hash

class User(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    role = db.Column(db.String(20), default="user")

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)