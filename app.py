from flask import Flask, render_template, flash
from admin import admin
from flask_login import LoginManager
from config import Config

from db import User

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    from db import db, migrate, Phones
    db.init_app(app)
    migrate.init_app(app, db)

    # Инициализация Flask-Login
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'  # Указываем endpoint для страницы входа

    # Регистрация Blueprint
    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from feedback import fb
    from main import main
    app.register_blueprint(main, url_prefix='/')
    app.register_blueprint(fb, url_prefix='/feedback')
    app.register_blueprint(admin, url_prefix='/admin')
    return app


if __name__ == "__main__":
    create_app().run("0.0.0.0", debug=True)
