# Python imports

# Flask imports
from controller import db

# Project imports


__Author__ = "Amir Mohammad"


class Announcement(db.Model):
    __tablename__ = 'announcements'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Unicode, unique=True, nullable=False)
    description = db.Column(db.Unicode, nullable=True)
    mobile_number = db.Column(db.String(13), nullable=True)
    lat = db.Column(db.Float, nullable=True)
    long = db.Column(db.Float, nullable=True)
    deposit_amount = db.Column(db.BigInteger, nullable=True)
    rent_amount = db.Column(db.BigInteger, nullable=True)
    has_loan = db.Column(db.Boolean)
    size_amount = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String),
    rooms_num = db.Column(db.Unicode, nullable=True, default=1)
    build_year = db.Column(db.DateTime, nullable=False)
    email = db.Column(db.String(254), nullable=True)
    market = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Announcement {}>'.format(self.title)
