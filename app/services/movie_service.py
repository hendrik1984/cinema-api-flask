from app.models.movie import Movie
from app.extensions import db
from math import ceil

class MovieService:

    @staticmethod
    def create_movie(title, description=None, duration=None):
        movie = Movie(
            title=title,
            description=description,
            duration=duration
        )

        db.session.add(movie)
        db.session.commit()

        return movie

    @staticmethod
    def get_all_movies(active_only=True):
        query = Movie.query

        if active_only:
            query = query.filter_by(is_active=True)

        return query.all()

    @staticmethod
    def get_movie_by_id(movie_id):
        movie = Movie.query.get(movie_id)

        if not movie:
            raise ValueError("Movie not found")

        return movie

    @staticmethod
    def update_movie(movie_id, **kwargs):
        movie = Movie.query.get(movie_id)

        if not movie:
            raise ValueError("Movie not found")

        if "title" in kwargs:
            movie.title = kwargs["title"]

        if "description" in kwargs:
            movie.description = kwargs["description"]

        if "duration" in kwargs:
            movie.duration = kwargs["duration"]

        if "is_active" in kwargs:
            movie.is_active = kwargs["is_active"]

        db.session.commit()
        return movie

    @staticmethod
    def delete_movie(movie_id):
        movie = Movie.query.get(movie_id)

        if not movie:
            raise ValueError("Movie not found")

        db.session.delete(movie)
        db.session.commit()

        return True

    @staticmethod
    def get_movies_paginated(page=1, limit=10, active_only=True):
        query = Movie.query

        if active_only:
            query = query.filter_by(is_active=True)

        total = query.count()

        movies = query \
            .order_by(Movie.created_at.desc()) \
            .offset((page - 1) * limit) \
            .limit(limit) \
            .all()

        total_pages = ceil(total / limit) if limit else 1

        return {
            "items": movies,
            "meta": {
                "page": page,
                "limit": limit,
                "total": total,
                "total_pages": total_pages
            }
        }