from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128))
    password = db.Column(db.String(128))
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Phones(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(30))
    name = db.Column(db.String(30))
    number = db.Column(db.String(12))


class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(30), default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    type = db.Column(db.String(10))
    name = db.Column(db.String(128))
    email = db.Column(db.String(128))
    message = db.Column(db.String(500))


class Pages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(30), default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    name = db.Column(db.String(128))
    url = db.Column(db.String(128))
    description = db.Column(db.String(10000))