from app.models.seat import Seat
from app.extensions import db

class SeatService:

    @staticmethod
    def create_seat(theater_id, row, number, seat_type):
        seat = Seat(
            theater_id=theater_id,
            row=row,
            number=number,
            seat_type=seat_type
        )

        db.session.add(seat)
        db.session.commit()

        return seat

    @staticmethod
    def get_seats(theater_id=None):
        query = Seat.query

        if theater_id:
            query = query.filter_by(theater_id=theater_id)

        return query.order_by(Seat.row, Seat.number).all()

    @staticmethod
    def get_seat_by_id(seat_id):
        return Seat.query.get(seat_id)

    @staticmethod
    def update_seat(seat, **kwargs):
        seat.row = kwargs("row")
        seat.number = kwargs("number")
        seat.seat_type = kwargs("seat_type")

        db.session.commit()
        return seat

    @staticmethod
    def delete_seat(seat):
        db.session.delete(seat)
        db.session.commit()