from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

from app.database.enums import ON_OFF

db = SQLAlchemy()


# an example
class Company(db.Model):
    __tablename__ = "companies"
    id = db.Column(db.Integer, primary_key=True)
    nick = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(20), unique=True, nullable=False)
    channel_id = db.Column(db.BigInteger, nullable=False)
    owner = db.Column(db.String(20), nullable=True)
    phones = db.Column(db.String(100), nullable=True)
    tg_id = db.Column(db.Integer, nullable=False)
    reg_date = db.Column(db.DateTime, server_default=func.now(), nullable=False)
    card = db.Column(db.String(200), nullable=False)
    default_percent = db.Column(db.Integer, server_default="20", nullable=False)
    phone_prefix = db.Column(db.String(5), server_default="+380", nullable=False)
    password = db.Column(db.String(32), nullable=False)
    sms = db.Column(db.Enum(ON_OFF), server_default="OFF", nullable=False)
    auto_lock = db.Column(db.Enum(ON_OFF), server_default="OFF")
    masters = db.relationship("MasterGlobal", secondary="masters_attachment")
