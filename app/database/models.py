from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref

from app.database.enums import W_D, B_S, A_InA

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    open_key = db.Column(db.String(64), unique=True)
    private_key = db.Column(db.String(64), unique=True)
    login = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)

    coins = db.relationship("UserCoin")
    wallets = db.relationship("WalletHistory")
    stakans = db.relationship("Stakan")


class Coin(db.Model):
    __tablename__ = "coins"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    icon_class = db.Column(db.String(100), nullable=True)


class UserCoin(db.Model):
    __tablename__ = "coins_of_user"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    coin_id = db.Column(db.Integer, db.ForeignKey("coins.id"), nullable=False)
    balance = db.Column(db.Float, nullable=False)

    user = db.relationship(User, backref=backref("coins_of_user", cascade="all, delete-orphan"))
    coin = db.relationship("Coin")


class WalletHistory(db.Model):
    __tablename__ = "wallet_history"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    coin_id = db.Column(db.Integer, db.ForeignKey("coins.id"), nullable=False)
    count = db.Column(db.Float, nullable=False)
    operation = db.Column(db.Enum(W_D), server_default="W")

    coin = db.relationship(Coin, backref=backref("wallet_history", cascade="all, delete-orphan"))


# wh.coin.balance

coins_from = db.Table('coins_from', db.metadata,
                      db.Column('stakan_id', db.Integer, db.ForeignKey('stakan.id')),
                      db.Column('coin_id', db.Integer, db.ForeignKey('coins.id'))
                      )

coins_to = db.Table('coins_to', db.metadata,
                    db.Column('stakan_id', db.Integer, db.ForeignKey('stakan.id')),
                    db.Column('coin_id', db.Integer, db.ForeignKey('coins.id'))
                    )


class Stakan(db.Model):
    __tablename__ = "stakan"
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Enum(B_S), server_default="B")
    count = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)
    status = db.Column(db.Enum(A_InA), server_default="InA")
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    coinsFrom = db.relationship("Coin", secondary=coins_from)
    coinsTo = db.relationship("Coin", secondary=coins_to)
