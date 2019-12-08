import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config


db = SQLAlchemy()
migrate = Migrate()


def create_app(config_name='default'):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config[config_name])
    app.config.from_pyfile('config.py', silent=True)

    db.init_app(app)
    migrate.init_app(app, db)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def hello():
        return 'Hello, World!'
    
    return app
