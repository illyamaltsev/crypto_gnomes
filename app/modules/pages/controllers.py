from . import pages


@pages.route("/")
def page():
    return 'Page'
