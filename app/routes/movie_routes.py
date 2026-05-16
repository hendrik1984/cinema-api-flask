from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from app.services.movie_service import MovieService
from app.utils.response import api_response
from app.utils.decorators import admin_required

movie_bp = Blueprint("movies", __name__)

@movie_bp.route("/", methods=["POST"])
@jwt_required()
@admin_required
def create_movie():
    data = request.json

    movie = MovieService.create_movie(
        title=data["title"],
        description=data.get("description"),
        duration=data.get("duration")
    )

    return api_response(
        data={
            "id": movie.id,
            "title": movie.title, 
            "description": movie.description,
        },
        message=f"Movie {movie.title} created",
        status_code=201
    )

@movie_bp.route("/", methods=["GET"])
def get_movies():
    # query params
    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 10))
    active_only = request.args.get("active_only", "true").lower() == "true"

    # validation negative page
    if page < 1:
        page = 1

    # validation limit should not exceed 50
    if limit > 50:
        limit = 50

    results = MovieService.get_movies_paginated(page=page, limit=limit, active_only=active_only)
    movies = results["items"]
    meta = results["meta"]

    data = [
        {
            "id": m.id,
            "title": m.title,
            "duration": m.duration,
            "is_active": m.is_active,
            "created_at": m.created_at.isoformat()
        }
        for m in movies
    ]

    return api_response(data=data,meta=meta)

@movie_bp.route("/<int:movie_id>", methods=["GET"])
def get_movie(movie_id):
    try:
        m = MovieService.get_movie_by_id(movie_id)

        return api_response(data={
            "id": m.id,
            "title": m.title,
            "description": m.description,
            "duration": m.duration,
            "is_active": m.is_active
        })

    except ValueError as e:
        return api_response(error=str(e), status_code=404)
    
@movie_bp.route("/<int:movie_id>", methods=["PUT"])
@jwt_required()
@admin_required
def update_movie(movie_id):
    data = request.json

    try:
        m = MovieService.update_movie(movie_id, **data)

        return api_response(
            data={
                "id": m.id,
                "title": m.title,
                "description": m.description,
                "duration": m.duration,
                "is_active": m.is_active
            },
            message=f"Movie {m.title} updated"
        )

    except ValueError as e:
        return api_response(error=str(e), status_code=404)
    
@movie_bp.route("/<int:movie_id>", methods=["DELETE"])
@jwt_required()
@admin_required
def delete_movie(movie_id):
    try:
        MovieService.delete_movie(movie_id)

        return api_response(message="Movie deleted")

    except ValueError as e:
        return api_response(error=str(e), status_code=404)