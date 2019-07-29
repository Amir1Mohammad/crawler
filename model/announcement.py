# -*- coding: utf-8 -*-
# Python imports

# Flask imports
from datetime import datetime
from controller import db

# Project imports


__Author__ = "Amir Mohammad"


class Announcement(db.Model):
    __tablename__ = 'announcements'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Unicode, nullable=False)
    description = db.Column(db.Unicode, nullable=True)
    url = db.Column(db.String(256), nullable=True)
    token = db.Column(db.String(32), nullable=False)
    mobile_number = db.Column(db.String(13), nullable=True)
    owner = db.Column(db.Unicode, nullable=True)
    place = db.Column(db.Unicode, nullable=True)
    rent = db.Column(db.Unicode, nullable=True)
    deposit_amount = db.Column(db.Unicode, nullable=True)
    price = db.Column(db.Unicode, nullable=True)
    lat = db.Column(db.Float, nullable=True)
    long = db.Column(db.Float, nullable=True)
    has_loan = db.Column(db.Boolean, default=False)
    size_amount = db.Column(db.Integer, nullable=False)
    type = db.Column(db.Unicode, nullable=False)
    rooms_num = db.Column(db.Integer, nullable=True, default=1)
    build_year = db.Column(db.Integer, nullable=True)
    market = db.Column(db.String(32), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return '<Announcement {} {}>'.format(self.mobile_number, self.created_at)

    def to_dict(self):
        data = {
            'id': self.id,
            'title': self.title,
            'url': self.url,
            'lat': self.lat,
            'long': self.long,
            'place': self.place,
            'rent': self.rent,
            'deposit_amount': self.deposit_amount,
            'price': self.price,
            'description': self.description,
            'mobile_number': self.mobile_number,
            'size_amount': self.size_amount,
            'type': self.type,
            'rooms_num': self.rooms_num,
            'build_year': self.build_year,
            'owner': self.owner,
            'created_at': self.created_at

        }
        return data
