from models import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Users(UserMixin, db.Model):
    __tablename__ = "users"

    # Primary Key
    id = db.Column(db.Integer, primary_key=True)

    # Auth
    email = db.Column(db.String(150), nullable=False, unique=True)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25))
    phone_number = db.Column(db.String(20))
    password = db.Column(db.String(105), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    bio = db.Column(db.String(1000), nullable=True)
    birthdate = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(50))
    interested_in = db.Column(db.String(50))
    height_cm = db.Column(db.Integer)
    location = db.Column(db.String(100))
    # Account Status
    is_active = db.Column(db.Boolean, default=True)
    is_verified = db.Column(db.Boolean, default=False)

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return f"<User {self.email}>"