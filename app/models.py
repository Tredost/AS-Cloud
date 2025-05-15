from datetime import date, datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

# associacao N-N entre exposicões e obras
exhibition_artwork = db.Table(
    'exhibition_artwork',
    db.Column('exhibition_id', db.Integer, db.ForeignKey('exhibition.id'), primary_key=True),
    db.Column('artwork_id',     db.Integer, db.ForeignKey('artwork.id'),     primary_key=True)
)

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id            = db.Column(db.Integer, primary_key=True)
    username      = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    created_at    = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username!r}>'

class Artist(db.Model):
    __tablename__ = 'artist'
    id            = db.Column(db.Integer, primary_key=True)
    name          = db.Column(db.String(100), nullable=False, unique=True)
    biography     = db.Column(db.Text)
    birth_date    = db.Column(db.Date)

    artworks      = db.relationship('Artwork', back_populates='artist', lazy=True)

    def __repr__(self):
        return f"<Artist {self.name!r}>"

class Artwork(db.Model):
    __tablename__ = 'artwork'
    id            = db.Column(db.Integer, primary_key=True)
    title         = db.Column(db.String(150), nullable=False)
    description   = db.Column(db.Text)
    creation_date = db.Column(db.Date)
    image_url     = db.Column(db.String(200), nullable=False)

    artist_id     = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
    artist        = db.relationship('Artist', back_populates='artworks', lazy=True)

    exhibitions   = db.relationship(
        'Exhibition', secondary=exhibition_artwork,
        back_populates='artworks', lazy='subquery'
    )

    def __repr__(self):
        return f"<Artwork {self.title!r} by {self.artist.name!r}>"

class Exhibition(db.Model):
    __tablename__ = 'exhibition'
    id            = db.Column(db.Integer, primary_key=True)
    name          = db.Column(db.String(120), nullable=False, unique=True)
    description   = db.Column(db.Text)
    date          = db.Column(db.Date, default=date.today)

    artworks      = db.relationship(
        'Artwork', secondary=exhibition_artwork,
        back_populates='exhibitions', lazy='subquery'
    )

    def __repr__(self):
        return f"<Exhibition {self.name!r} on {self.date}>"
