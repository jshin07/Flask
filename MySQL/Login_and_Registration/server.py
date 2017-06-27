from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
from sqlalchemy.sql import text

import re

app = Flask(__name__)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app.secret_key = 'secret_key'
mysql= MySQLConnector(app, 'email_db')
bcrypt=Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    login_email= request.form['login_email']
    password= request.form['password']
    invalid=False
    user= mysql.query_db("SELECT * FROM users WHERE email = '{}'".format(login_email))
    if not EMAIL_REGEX.match(login_email):
        invalid=True
        flash("Invalid Email")
    if len(user)<1:
        flash("You are not in our database")
    if len(password) <9 :
        invalid=True
        flash("Password must be at least 8 characters")
    if password != request.form['password_conf']:
        invalid=True
        flash ("Password doesn't match")
    if bcrypt.check_password_hash(user[0]['pw'], password) == False:
        invalid=True
        flash ("Incorrect password")
    if invalid:
        return redirect ('/')
    else:
        return render_template('success.html')


@app.route('/register', methods=['POST'])
def register():
    first_name= request.form['first_name']
    last_name= request.form['last_name']
    email= request.form['email']
    reg_password= request.form['reg_password']
    reg_password_conf= request.form['reg_password_conf']
    invalid=False
    user= mysql.query_db("SELECT * FROM users WHERE email = '{}'".format(email))
    if len(first_name) <2:
        invalid=True
        flash("First name has to be at least 2 characters")
    if type(first_name) == int:
        invalid=True
        flash("First name cannot contanin numbers")
    if len(last_name) <2:
        invalid=True
        flash("Last name has to be at least 2 characters")
    if type(last_name) == int:
        invalid=True
        flash("Last name cannot contanin numbers")
    if not EMAIL_REGEX.match(email):
        invalid=True
        flash("Invalid Email")
    # if user[0]['email']==email:  --- This checks the database and finds if they are already registered, but with this block, I can't register. Out of index error?
    #     invalid=True
    #     flash("You already registered. Please login")
    if len(reg_password) <9 :
        invalid=True
        flash("Please put at least 8 characters")
    if reg_password != reg_password_conf:
        invalid=True
        flash ("Password doesn't match")
    if invalid:
        return redirect ('/')
    else:
        hash= bcrypt.generate_password_hash('reg_password')
        query="INSERT INTO users (email, pw, created_at, updated_at) VALUES (:email, :pw, NOW(), NOW())"
        data= {
            "email": email,
            "pw": hash
        }
        mysql.query_db(query, data)
        return render_template('success.html')


app.run(debug=True)
