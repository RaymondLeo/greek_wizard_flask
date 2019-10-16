# project/__init__.py
from flask import Flask
from models.shared import db

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    return app

# TODO: Make this a custom command.
def create_db():
    with create_app().app_context():
        from models.user import User
        db.create_all()
