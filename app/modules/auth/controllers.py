from hashlib import md5

from flask import request, session, redirect, url_for, escape, Response

from app.database.models import User
from . import authBP


def get_md5(string):
    m = md5()
    m.update(string.encode("utf-8"))
    return m.hexdigest()


@authBP.route("/auth/", methods=["POST"])
def auth():
    """ View that handles authentication.
    """
    login = request.form["login"]
    password = request.form["password"]

    user = User.query.filter_by(login=login).first()

    if user and user.password == password:
        session["user_id"] = user.id
        return redirect(url_for("pages.user"))
    else:
        return Response("Bad login or pass!", status=401)


@authBP.route("/logout/", methods=["GET"])
def logout():
    """ View that handles logout.
    """
    session.pop("user_id", None)
    return redirect(url_for("pages.login"))
