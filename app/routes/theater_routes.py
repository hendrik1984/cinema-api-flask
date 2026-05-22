from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from app.services.theater_service import TheaterService
from app.utils.response import api_response
from app.utils.decorators import admin_required

theater_bp = Blueprint("theater", __name__, url_prefix="/theaters")

@theater_bp.route("", methods=["POST"])
@jwt_required()
@admin_required
def create():
    data = request.get_json()
    name = data.get("name")

    theater_find = TheaterService.get_theater_by_name(name)

    if theater_find:
        return api_response(message=f"Duplicate Theater name {name}")

    theater = TheaterService.create_theater(
        name = name
    )

    return api_response(data={
            "id": theater.id,
            "name": theater.name
        }, status_code=201)


@theater_bp.route("", methods=["GET"])
@jwt_required()
def get_all():
    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 10))

    theaters, total = TheaterService.get_theaters(page, limit)

    return api_response(data=[
            {"id": t.id, "name": t.name}
            for t in theaters
        ],
        meta={"page": page, "total": total}
    )


@theater_bp.route("/<int:theater_id>", methods=["GET"])
@jwt_required()
def get_detail(theater_id):
    theater = TheaterService.get_theater_by_id(theater_id)

    if not theater:
        return api_response(error="Theater not found")

    return api_response(data={
            "id": theater.id,
            "name": theater.name
        })


@theater_bp.route("/<int:theater_id>", methods=["PUT"])
@jwt_required()
def update(theater_id):
    theater = TheaterService.get_theater_by_id(theater_id)

    if not theater:
        return api_response(error="Theater not found")

    data = request.get_json()
    name = data.get("name")

    theater_find = TheaterService.get_theater_by_name(name)

    if theater_find:
        return api_response(message=f"Theater with name {name} is not available")

    theater = TheaterService.update_theater(theater_id, name)

    return api_response(data={
            "id": theater.id,
            "name": theater.name
        })


@theater_bp.route("/<int:theater_id>", methods=["DELETE"])
@jwt_required()
def delete(theater_id):
    theater = TheaterService.get_theater_by_id(theater_id)

    if not theater:
        return api_response(error=f"Theater not found {theater_id}")

    TheaterService.delete_theater(theater)

    return api_response(message=f"Theater deleted {theater.name}")