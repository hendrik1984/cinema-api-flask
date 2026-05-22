# app/routes/seat_routes.py

from flask import Blueprint, request
from app.services.seat_service import SeatService
from app.utils.response import api_response

seat_bp = Blueprint("seat", __name__, url_prefix="/seats")


@seat_bp.route("", methods=["POST"])
def create():
    data = request.json

    if data.get("theater_id") is None:
        return api_response(message="Theater id is missing", status_code=400)

    seat = SeatService.create_seat(
        theater_id=data.get("theater_id"),
        row=data.get("row"),
        number=data.get("number"),
        seat_type=data.get("seat_type")
    )

    return api_response(data={
            "id": seat.id,
            "theater_id": seat.theater_id,
            "row": seat.row,
            "number": seat.number,
            "seat_type": seat.seat_type
        }, status_code=201)


@seat_bp.route("", methods=["GET"])
def get_all():
    theater_id = request.json.get("theater_id")

    seats = SeatService.get_seats(theater_id)

    return api_response(
        data=[
            {
                "id": s.id,
                "theater_id": s.theater_id,
                "row": s.row,
                "number": s.number,
                "seat_type": s.seat_type
            }
            for s in seats
    ])


@seat_bp.route("/<int:seat_id>", methods=["GET"])
def get_detail(seat_id):
    seat = SeatService.get_seat_by_id(seat_id)

    if not seat:
        return api_response(error="Seat not found")

    return api_response(data={
        "id": seat.id,
        "theater_id": seat.theater_id,
        "row": seat.row,
        "number": seat.number,
        "seat_type": seat.seat_type
    })


@seat_bp.route("/<int:seat_id>", methods=["PUT"])
def update(seat_id):
    seat = SeatService.get_seat_by_id(seat_id)

    if not seat:
        return api_response(error="Seat not found")

    seat = SeatService.update_seat(seat, request.get_json())

    return api_response(data={
        "id": seat.id,
        "theater_id": seat.theater_id,
        "row": seat.row,
        "number": seat.number,
        "seat_type": seat.seat_type
    })


@seat_bp.route("/<int:seat_id>", methods=["DELETE"])
def delete(seat_id):
    seat = SeatService.get_seat_by_id(seat_id)

    if not seat:
        return api_response(error="Seat not found")

    SeatService.delete_seat(seat)

    return api_response(message="Seat deleted")