from flask import session, request, Response

from app.database.models import UserCoin, db
from . import api


@api.route('/api/create-wallet/', methods=['POST'])
def add_wallet():
    user_id = session.get('user_id')

    coin_id = request.json['value']

    uc = UserCoin(user_id=user_id, coin_id=coin_id, balance=0)
    db.session.add(uc)
    db.session.commit()
    return Response(uc.coin.name, 200)


@api.route('/api/do-withdraw/', methods=['POST'])
def do_withdraw():
    user_id = session.get('user_id')
    user_coin_id = request.form.get('user_coin_id')
    amount = request.form.get('amount')

    uc = UserCoin.query.get(user_coin_id)
    uc.balance -= amount
    db.session.commit()
    return Response('ok', 200)


@api.route('/api/do-deposit/', methods=['POST'])
def do_deposit():
    user_id = session.get('user_id')
    user_coin_id = request.form.get('user_coin_id')
    amount = request.form.get('amount')

    uc = UserCoin.query.get(user_coin_id)
    uc.balance += amount
    db.session.commit()
    return Response('ok', 200)


