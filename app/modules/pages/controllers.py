from flask import session, url_for, redirect, render_template

from app.modules.auth import login_required
from . import pages


@pages.route("/")
@pages.route("/login/")
def login():
    """ View that returns login template.
        All not authenticated requests redirected here.
        If session have info for login, it redirects to orders page.
    """
    # user_id = session.get('user_id', None)

    # if user_id and User.query.get(user_id):
    #    return redirect(url_for('pages.user', page='orders'))

    return render_template('authorization.html')


@login_required
@pages.route("/registration/")
def registration():
    """ View that returns user template.
    """
    user_id = session.get('user_id', None)

    # some user manipulation

    return render_template('registration.html')


@login_required
@pages.route("/user/")
def user():
    """ View that returns user template.
    """
    user_id = session.get('user_id', None)

    # some user manipulation

    return render_template('user.html')


@login_required
@pages.route("/stakan/")
def stakan():
    """ View that returns user template.
    """
    user_id = session.get('user_id', None)

    # some user and stakan manipulation

    return render_template('stakan.html')
