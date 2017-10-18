from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
#from sqlalchemy import Column, String, Integer, ForeignKey
from tempfile import gettempdir
# configure application
app = Flask(__name__)

#Flask-SQLAlchemy  https://www.tutorialspoint.com/flask/flask_sqlalchemy.htm
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///froshims3.db"
db = SQLAlchemy(app)

# configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = gettempdir()
app.config["SESSION_PERMANENT"] = False
Session(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String)
    hash = db.Column(db.String)

    def __init__(self, username, password):
      self.username = username
      self.password = password

#db.create_all()
