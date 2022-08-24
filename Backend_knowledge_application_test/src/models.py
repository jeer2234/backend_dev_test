from datetime import datetime
from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(150))
    email = db.Column(db.String(120), nullable=False,  index=True, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    posts = db.relationship('Publication', backref='author', lazy='dynamic')
    created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User {}>'.format(self.full_name)
    
    @property
    def serialized(self):
        """Return object data in serializeable format"""
        return {
            'full_name': self.full_name,
            'email': self.email,
        }


class Publication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    description = db.Column(db.String(150))
    body = db.Column(db.String(300))
    priority = db.Column(db.String(50))
    status = db.Column(db.String(50))

    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    published_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.description)
