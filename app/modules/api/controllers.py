from flask import session, request, Response

from app.database.enums import W_D
from app.database.models import UserCoin, db, WalletHistory, Stakan, Coin
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
    user_coin_id = int(request.form.get('user_coin_id'))
    amount = int(request.form.get('amount'))

    uc = UserCoin.query.get(user_coin_id)
    uc.balance -= amount

    wh = WalletHistory(user_id=user_id, coin_id=uc.coin.id, count=amount, operation=W_D.W)

    db.session.add(wh)
    db.session.commit()

    return Response('ok', 200)


@api.route('/api/do-deposit/', methods=['POST'])
def do_deposit():
    user_id = session.get('user_id')
    user_coin_id = int(request.form.get('user_coin_id'))
    amount = int(request.form.get('amount'))

    uc = UserCoin.query.get(user_coin_id)
    uc.balance += amount

    wh = WalletHistory(user_id=user_id, coin_id=uc.coin.id, count=amount, operation=W_D.D)

    db.session.add(wh)
    db.session.commit()
    return Response('ok', 200)


@api.route('/api/stakan/create/', methods=['POST'])
def do_stakan_create():
    user_id = session.get('user_id')
    type = request.form.get('type')
    from_coin_id = request.form.get('from')
    to_coin_id = request.form.get('to')
    price = request.form.get('price')
    count = request.form.get('count')

    coin_from = Coin.query_get(from_coin_id)
    coin_to = Coin.query_get(to_coin_id)

    new_stakan = Stakan(type=type, coinsFrom=coin_from, coinsTo=coin_to, price=price, user_id=user_id, count=count)
    db.session.add(new_stakan)
    db.session.commit()
    return Response('ok', 200)


@api.route('/api/stakan/buy/', methods=['POST'])
def do_stakan_buy():
    user_id = session.get('user_id')
    stakan_id = request.form.get('stakan_id')
    stakan = Stakan.query.get(stakan_id)

    db.session.commit()
    return Response('ok', 200)


@api.route('/api/stakan/delete/', methods=['POST'])
def do_stakan_delete():
    user_id = session.get('user_id')
    stakan_id = request.form.get('stakan_id')
    stakan = Stakan.query.get(stakan_id)

    db.session.delete(stakan)
    db.session.commit()
    return Response('ok', 200)
