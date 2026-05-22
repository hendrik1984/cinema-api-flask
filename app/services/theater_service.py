from app.models.theater import Theater
from app.extensions import db

class TheaterService:
    @staticmethod
    def create_theater(name):
        theater = Theater(name=name)
        
        db.session.add(theater)
        db.session.commit()

        return theater

    @staticmethod
    def get_theaters(page=1, limit=10):
        query = Theater.query

        total = query.count()

        theaters = query.offset((page - 1) * limit).limit(limit).all()

        return theaters, total

    @staticmethod
    def get_theater_by_id(theater_id):
        return Theater.query.get(theater_id)

    @staticmethod
    def get_theater_by_name(theater_name):
        return Theater.query.filter_by(name=theater_name).all()
    
    @staticmethod
    def update_theater(theater_id, name):
        theater = Theater.query.get(theater_id)
        theater.name = name

        db.session.commit()
        return theater

    @staticmethod
    def delete_theater(theater):
        db.session.delete(theater)
        db.session.commit()