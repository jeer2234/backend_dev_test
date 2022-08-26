from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from .app import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(150))
    email = db.Column(db.String(120), nullable=False, index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Publication', backref='author', lazy='dynamic')

    created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User {}>'.format(self.full_name)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
        

    def update_user(self, **kwargs):
        if kwargs:
            
            for parameter in kwargs:
                if parameter == 'full_name':
                    self.full_name = kwargs[parameter]
                
                if parameter == 'email':
                    self.email = kwargs[parameter]
                
                if parameter == 'password':
                    self.set_password(kwargs[parameter])
            
            db.session.add(self)
            db.session.commit()
        else:
            return None
            
    def json(self):
        return {'id': self.id, 'full_name': self.full_name, 'email': self.email}

    def delete_user(self):
        db.session.delete(self)
        db.session.commit()
        
    def add_user(_full_name, _email, _password_hash):
        """function to add movie to database using _title, _year, _genre
        as parameters"""
        # creating an instance of our Movie constructor
        new_user = User(full_name=_full_name, email=_email)
        new_user.set_password(_password_hash)
        db.session.add(new_user)  # add new movie to database session
        db.session.commit()  # commit changes to session
        return new_user


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
