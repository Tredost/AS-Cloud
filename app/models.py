# C:\Users\ianes\Desktop\AS Cloud\app\models.py

from datetime import datetime
from flask_login import UserMixin
from app import db
from sqlalchemy import Text

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id            = db.Column(db.Integer, primary_key=True)
    username      = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(Text, nullable=False)
    created_at    = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.username!r}>'

class Car(db.Model):
    __tablename__ = 'cars'
    id            = db.Column(db.Integer, primary_key=True)
    name          = db.Column(db.String(100), nullable=False)
    user_id       = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user          = db.relationship('User', backref=db.backref('cars', lazy=True))
    photo         = db.Column(db.String(200), nullable=False)
    description   = db.Column(db.Text, nullable=False)
    start_year    = db.Column(db.Integer, nullable=False)
    end_year      = db.Column(db.Integer, nullable=False)
    horsepower    = db.Column(db.Integer, nullable=False)
    torque        = db.Column(db.Integer, nullable=False)
    top_speed     = db.Column(db.Integer, nullable=False)
    drive_type    = db.Column(db.String(50), nullable=False)
    transmission  = db.Column(db.String(50), nullable=False)
    created_at    = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Car {self.id} by User {self.user_id}>'
