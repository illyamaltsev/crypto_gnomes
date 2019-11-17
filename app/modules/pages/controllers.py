from flask import session, url_for, redirect, render_template, request

from app.database.models import User, User_Coin, Wallet_History, Stakan, db, Coin, Coin_From, Coin_To
from app.modules.auth import login_required
from . import pages


@pages.route("/")
@pages.route("/login/")
def login():
    """ View that returns login template.
        All not authenticated requests redirected here.
        If session have info for login, it redirects to user page.
    """
    user_id = session.get('user_id', None)

    if user_id and User.query.get(user_id):
        return redirect(url_for('pages.user_page'))

    return render_template('authorization.html')


@pages.route("/registration/", methods=['GET', 'POST'])
def registration():
    """ View that returns registration template.
    """
    if request.method == 'POST':
        login = request.form["login"]
        password = request.form["password"]
        if User.query.filter_by(login=login).first():
            return redirect(url_for('pages.registration'))
        new_user = User(login=login, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('pages.login'))
    else:
        return render_template('registration.html')


@login_required
@pages.route("/user/")
def user_page():
    """ View that returns user template.
    """
    user_id = session.get('user_id', None)

    user = User.query.get(user_id)

    user_coins = User_Coin.query.filter_by(user_id=user_id).all()

    wallet_history = Wallet_History.query.filter_by(user_id=user_id).all()

    coins = Coin.query.all()

    return render_template('user.html', user=user, user_coins=user_coins, wallet_history=wallet_history, coins=coins)


@login_required
@pages.route("/stakan/")
def stakan():
    """ View that returns stakan template.
    """
    user_id = session.get('user_id', None)

    user = User.query.get(user_id)

    all_stakans = Stakan.query.all()

    user_stakans = Stakan.query.filter_by(user_id=user_id)

    coin_from = Coin_From.query.all()

    coin_to = Coin_To.query.all()



    return render_template('stakan.html', user=user, all_stakans=all_stakans, user_stakans=user_stakans, coin_from = coin_from, coin_to = coin_to )





