#from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import gettempdir
from datetime import *
#from sqlalchemy import Column, String, Integer, ForeignKey
from helpers import *

# configure application
app = Flask(__name__)

#Flask-SQLAlchemy  https://www.tutorialspoint.com/flask/flask_sqlalchemy.htm
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///froshims3.db"
app.config["SQLALCHEMY_ECHO"]= True
db = SQLAlchemy(app)
    
#ensure responses aren't cached (temporate memory)
# if app.config["DEBUG"]:
#     @app.after_request
#     def after_request(response):
#         response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
#         response.headers["Expires"] = 0
#         response.headers["Pragma"] = "no-cache"
#         return response

# custom filter
#app.jinja_env.filters["usd"] = usd

# configure session to use filesystem (instead of signed cookies)
# on session vs cookies : http://stackoverflow.com/questions/2240556/when-should-i-use-session-variables-instead-of-cookies
app.config["SESSION_FILE_DIR"] = gettempdir()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"     #causes that there is always a session-id, so acts like its logged in. 
Session(app)

class users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String)
    hash = db.Column(db.String)

    def __init__(self, username, password):
      self.username = username
      self.password = password

db.create_all()

# configure CS50 Library to use SQLite database
#db = SQL("sqlite:///whobringswhat.db")

@app.route("/")
#@login_required
def index():
    return apology("TODO")

@app.route("/login", methods=["GET", "POST"])
def login():
     return apology("TODO")

@app.route("/logout")
def logout():
    """Log user out."""
    return apology("TODO")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user."""
    if request.method == "GET":
        # redirect user to register page
        return render_template("register.html")
        
    # if request.method == "POST":
    else: 
        # ensure username and passwords were submitted
        if request.form["username"] == "" :
            # or request.form["password2"] ="" 
            #or request.form["password"] ="" 
            return apology("username and password need to be filled in")
        # query database to see if username doesn't exist.
        rows = db.session.query("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))
        if len(rows) == 1:
            return apology("username already exist")
  
        elif request.form.get("password") != request.form.get("password2"):
            return apology("the passwords are not the same. Make sure your repeated password is the same as the first one.") 
        # hash: http://stackoverflow.com/questions/7627752/secure-authentication-system-in-python
        hash = pwd_context.encrypt(request.form["password"])
        # execute : http://stackoverflow.com/questions/3535532/python-doesnt-save-data-to-sqlite-db
        #id= db.Column(db.Integer, primary_key=True)
        user = users(request.form["username"], request.form["dorm"])
        db.session.add(user)
        db.session.commit()
        #rows = db.execute("INSERT INTO users (username, hash) VALUES(:username, :hash)", username=request.form.get("username"), hash=hash)
        # user_id : http://cs50.stackexchange.com/questions/23468/confusion-on-sessionuser-id-rows0id-pset7
        # http://pythoncentral.io/introduction-to-sqlite-in-python/
        user_id = db.session.query("SELECT id from users WHERE username = :username", username=request.form.get("username"))
        session["user_id"]= user_id
       # return redirect(url_for("quote"))
        
        #difference between render and redirect to login?
        #how does it know to make an row named id with a primary key? 
    return apology("Well Done")
        

@app.route("/newParty", methods=["GET", "POST"])
#@login_required
def newParty():
    """Sell shares of stock."""
    return apology("TODO")
    
@app.route("/myParties", methods=["GET", "POST"])
#@login_required
def myParties():
    """Sell shares of stock."""
    return apology("TODO")
