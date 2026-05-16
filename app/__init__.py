from flask import Flask
from .config import Config
from .extensions import db, jwt, migrate
from app.command.seed import seed_cli

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    #User Routes
    from .routes.user_routes import user_bp
    app.register_blueprint(user_bp, url_prefix="/users")
    
    #Movie Routes
    from .routes.movie_routes import movie_bp
    app.register_blueprint(movie_bp, url_prefix="/movies")

    app.cli.add_command(seed_cli)

    return app