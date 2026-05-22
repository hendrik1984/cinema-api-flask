from app.extensions import db
from datetime import datetime, timezone

class BaseModel(db.Model):
    __abstract__ = True

    created_at = db.Column(
        db.DateTime,
        default=datetime.now(timezone.utc),
        nullable=False
    )

    updated_at = db.Column(
        db.DateTime,
        default=datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False
    )