import os

from flask import Flask

from .views import pages

def create_app():
    app = Flask(__name__)
    key = os.urandom(24)

    app.secret_key = "DEV" if app.debug else key
    app.jinja_env.add_extension('jinja2.ext.do')

    app.register_blueprint(pages.bp)

    return app

    