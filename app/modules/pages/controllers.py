from flask import session, url_for, redirect, render_template

from app.database.models import User, User_Coin, Wallet_History, Stakan
from app.modules.auth import login_required
from . import pages


@pages.route("/")
@pages.route("/login/")
def login():
    """ View that returns login template.
        All not authenticated requests redirected here.
        If session have info for login, it redirects to user page.
    """
    # user_id = session.get('user_id', None)

    # if user_id and User.query.get(user_id):
    #    return redirect(url_for('pages.user', page='orders'))

    return render_template('authorization.html')


@pages.route("/registration/")
def registration():
    """ View that returns registration template.
    """

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

    return render_template('user.html', user=user, user_coins=user_coins, wallet_history=wallet_history)


@login_required
@pages.route("/stakan/")
def stakan():
    """ View that returns stakan template.
    """
    user_id = session.get('user_id', None)

    user = User.query.get(user_id)

    all_stakans = Stakan.query.all()

    user_stakans = Stakan.query.filter_by(user_id=user_id)

    return render_template('stakan.html', user=user, all_stakans=all_stakans, user_stakans=user_stakans)
