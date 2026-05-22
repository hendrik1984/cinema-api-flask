from app.extensions import db
from app.models.base import BaseModel

class Seat(BaseModel):
    __tablename__ = "seats"

    id = db.Column(db.Integer, primary_key=True)

    theater_id = db.Column(db.Integer, db.ForeignKey("theaters.id"), nullable=False)

    row = db.Column(db.String(5), nullable=False)

    number = db.Column(db.String(10), nullable=False)  # A1, B3, etc

    seat_type = db.Column(db.String(50), nullable=True)  # optional (VIP, Regular)

    __table_args__ = (
        db.UniqueConstraint("theater_id", "row", "number"),
    )

    @property
    def seat_label(self):
        return f"{self.row}{self.number}"
    