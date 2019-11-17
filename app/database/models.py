from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref

from app.database.enums import W_D, B_S

db = SQLAlchemy()


 class User(db.Model):
        __tablename__ = "users"
        id = db.Column(db.Integer, primary_key=True)
        open_key = db.Column(db.String(20), unique=True, nullable=False)
        private_key = db.Column(db.String(20), unique=True, nullable=False)
        login = db.Column(db.String(20), nunique=True, nullable=False)
        password = db.Column(db.String(20), unique=True, nullable=False)
        coins = db.relationship("Coin", secondary="coins_of_user")
        wallets = db.relationship("User", secondary="wallet_history")

class Coin(db.Model):
        __tablename__ = "coins"
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(100), nullable=True)
        users = db.relationship("User", secondary="coins_of_user")
        users_wallet = db.relationship("User", secondary="wallet_history")

class User_Coin(db.Model):
        __tablename__ = "coins_of_user"
        id = db.Column(db.Integer, primary_key=True)
        user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
        coin_id = db.Column(db.Integer, db.ForeignKey("coins.id"), nullable=False)
        user = db.relationship(User, backref=backref("coins_of_user", cascade="all, delete-orphan"))
        coin = db.relationship(Coin, backref=backref("coins_of_user", cascade="all, delete-orphan"))
        balance = db.Column(db.Float, nullable=False)



class Wallet_History(db.Model):
        __tablename__ = "wallet_history"
        id = db.Column(db.Integer, primary_key=True)
        user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
        coin_id = db.Column(db.Integer, db.ForeignKey("coins.id"), nullable=False)
        user = db.relationship(User, backref=backref("wallet_history", cascade="all, delete-orphan"))
        coin = db.relationship(Coin, backref=backref("wallet_history", cascade="all, delete-orphan"))
        count = db.Column(db.Float, nullable=False)
        operation = db.Column(db.Enum(W_D), server_default="W")

class Stakan(db.Model):
    __tablename__ = "stakan"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    user = db.relationship(User, backref=backref("wallet_history", cascade="all, delete-orphan"))
    coin = db.relationship(Coin, backref=backref("wallet_history", cascade="all, delete-orphan"))
    count = db.Column(db.Float, nullable=False)

    type = db.Column(db.Enum(B_S), server_default="B")