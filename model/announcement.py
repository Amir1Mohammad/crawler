# Python imports

# Flask imports
from controller import db

# Project imports


__Author__ = "Amir Mohammad"


class Announcement(db.Model):
    __tablename__ = 'announcements'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Unicode, nullable=False)
    description = db.Column(db.Unicode, nullable=True)
    mobile_number = db.Column(db.String(13), nullable=True)
    lat = db.Column(db.Float, nullable=True)
    long = db.Column(db.Float, nullable=True)
    district = db.Column(db.Unicode, nullable=True)
    deposit_amount = db.Column(db.Unicode, nullable=True)
    rent_amount = db.Column(db.Unicode, nullable=True)
    has_loan = db.Column(db.Boolean, default=False)
    size_amount = db.Column(db.Unicode, nullable=False)
    type = db.Column(db.Unicode, nullable=False)
    rooms_num = db.Column(db.Unicode, nullable=True, default=1)
    build_year = db.Column(db.Unicode, nullable=False)
    market = db.Column(db.String(32), nullable=False)
    send_sms = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=False)
    third = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<Announcement {}>'.format(self.title)

    def to_dict(self):
        data = {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'mobile_number': self.mobile_number,
            'size_amount': self.size_amount,
            'type': self.type,
            'rooms_num': self.rooms_num,
            'build_year': self.build_year,
            'district': self.district,
            'lat': self.lat,
            'long': self.long,
            'deposit_amount': self.deposit_amount

        }

        return data
