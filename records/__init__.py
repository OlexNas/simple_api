from flask import Flask
from .extensions import db
import os


DB_NAME = 'records.db'
def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)
    db.init_app(app)

    from .models import Author, Genre, Song
    from .api import api

    app.register_blueprint(api, url_prefix='/')

    create_tables(app)

    return app



def create_tables(app):
    with app.app_context():

        if not os.path.exists(os.path.join(os.getcwd(), f"instance/{DB_NAME}")):
            print(os.getcwd())
            db.create_all()
            print(f"Database {DB_NAME} created!")







