from flask.cli import AppGroup
from app.extensions import db
from app.models.user import User

seed_cli = AppGroup("seed")


@seed_cli.command("admin")
def seed_admin():
    """Create default admin user"""

    email = "admin@gmail.com"
    username = "admin"
    password = "password"

    existing_user = User.query.filter_by(email=email).first()

    if existing_user:
        print("Admin already exists")
        return

    admin = User(
        email=email,
        username=username,
        role="admin"
    )
    admin.set_password(password)

    db.session.add(admin)
    db.session.commit()

    print("Admin user created:")
    print(f"Email: {email}")
    print(f"Password: {password}")