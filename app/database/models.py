from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref

from app.database.enums import W_D, B_S, A_InA

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    open_key = db.Column(db.String(20), unique=True, nullable=True)
    private_key = db.Column(db.String(20), unique=True, nullable=True)
    login = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    coins = db.relationship("Coin", secondary="coins_of_user")
    wallets = db.relationship("Coin", secondary="wallet_history")
    stakans = db.relationship("Coin", secondary="stakan")


class Coin(db.Model):
    __tablename__ = "coins"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    users = db.relationship("User", secondary="coins_of_user")
    users_wallet = db.relationship("User", secondary="wallet_history")
    stakans = db.relationship("User", secondary="stakan")
    coinsFrom = db.relationship("Stakan", secondary="coins_from")
    coinsTo = db.relationship("Stakan", secondary="coins_to")


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

# wh.coin.balance


class Stakan(db.Model):
    __tablename__ = "stakan"
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Enum(B_S), server_default="B")
    count = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)
    status = db.Column(db.Enum(A_InA), server_default="InA")
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    coinsFrom = db.relationship("Coin_From", secondary="coins_from")
    coinsTo = db.relationship("Coin_To", secondary="coins_to")
    user = db.relationship(User, backref=backref("stakan", cascade="all, delete-orphan"))


class Coin_From(db.Model):
    __tablename__ = "coins_from"
    id = db.Column(db.Integer, primary_key=True)
    stakan_id = db.Column(db.Integer, db.ForeignKey("stakan.id"), nullable=False)
    coin_id = db.Column(db.Integer, db.ForeignKey("coins.id"), nullable=False)
    coin = db.relationship(Coin, backref=backref("coins_from", cascade="all, delete-orphan"))
    from_coin = db.relationship(Stakan, backref=backref("coins_from", cascade="all, delete-orphan"))


class Coin_To(db.Model):
    __tablename__ = "coins_to"
    id = db.Column(db.Integer, primary_key=True)
    stakan_id = db.Column(db.Integer, db.ForeignKey("stakan.id"), nullable=False)
    coin_id = db.Column(db.Integer, db.ForeignKey("coins.id"), nullable=False)
    coinTo = db.relationship(Coin, backref=backref("coins_to", cascade="all, delete-orphan"))
    coinStakan = db.relationship(Stakan, backref=backref("coins_to", cascade="all, delete-orphan"))