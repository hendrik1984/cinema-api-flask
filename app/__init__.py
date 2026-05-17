from flask import Flask, request, Response
from .config import Config
from .extensions import db, jwt, migrate
from app.command.seed import seed_cli
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    CORS(app)
    
    #User Routes
    from .routes.user_routes import user_bp
    app.register_blueprint(user_bp, url_prefix="/users")
    
    #Movie Routes
    from .routes.movie_routes import movie_bp
    app.register_blueprint(movie_bp, url_prefix="/movies")

    @app.before_request
    def handle_preflight():
        if request.method == "OPTIONS":
            res = Response()
            res.headers["X-Content-Type-Options"] = "*"
            return res

    app.cli.add_command(seed_cli)

    return app