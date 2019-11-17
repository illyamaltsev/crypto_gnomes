from flask import session, request, Response

from app.database.models import User_Coin, db
from . import api


@api.route('/api/create-wallet/', methods=['POST'])
def add_wallet():
    user_id = session.get('user_id')

    coin_id = request.json['value']

    uc = User_Coin(user_id=user_id, coin_id=coin_id, balance=0)
    db.session.add(uc)
    db.session.commit()
    return Response(uc.coin.name, 200)


@api.route('/api/do-withdraw/', methods=['POST'])
def do_withdraw():
    user_id = session.get('user_id')

    return Response('lol', 200)
