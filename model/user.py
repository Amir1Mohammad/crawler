# Python imports
from datetime import datetime

# Flask imports
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask import url_for
# Project imports
from controller import db
from controller import login

__Author__ = "Amir Mohammad"


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))


class Log(db.Model):
    __tablename__ = 'logs'

    id = db.Column(db.Integer, primary_key=True)
    announcement_id = db.Column(db.Integer, db.ForeignKey('announcements.id'), nullable=False, index=True)
    is_seen = db.Column(db.Boolean, default=False)
    is_submit = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    status = db.Column(db.Boolean, default=False)  # Checking status

    def __repr__(self):
        return '<Log {} {} {}>'.format(self.created_at, self.announcement_id, self.is_seen)

    @property
    def log_to_dict(self):
        data = {
            'id': self.id,
            'created_at': self.created_at,
            'announcement': 'announcement',
            'status': self.status,
            'is_seen': self.is_seen,
            'is_submit': self.is_submit,
        }
        return data
