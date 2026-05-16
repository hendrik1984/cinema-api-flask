from app.extensions import db
from app.models.base import BaseModel

class Movie(BaseModel):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)
    duration = db.Column(db.Integer)  # minutes

    is_active = db.Column(db.Boolean, default=True)