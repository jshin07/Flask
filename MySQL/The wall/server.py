from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
from sqlalchemy.sql import text

import re

app = Flask(__name__)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app.secret_key = 'secret_key'
mysql= MySQLConnector(app, 'thewall_db')
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
        invalid=True
        flash("You are not in our database")
        return redirect ('/')
    if len(password) <9 :
        invalid=True
        flash("Password must be at least 8 characters")
    if password != request.form['password_conf']:
        invalid=True
        flash ("Password doesn't match")
    if not bcrypt.check_password_hash(user[0]['password'], password) :
        invalid=True
        flash ("Incorrect password")
    if invalid:
        return redirect ('/')
    else:
        session['user_id']= user[0]['id']
        session['name']=user[0]['first_name']
        return redirect('/wall')


@app.route('/register', methods=['POST'])
def register():
    first_name= request.form['first_name']
    last_name= request.form['last_name']
    email= request.form['email']
    reg_password= request.form['reg_password']
    reg_password_conf= request.form['reg_password_conf']
    invalid=False
    user = mysql.query_db("SELECT * FROM users WHERE email = '{}'".format(email))

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
    if len(user) > 1 :
        invalid=True
        flash("You already registered. Please login")
    if len(reg_password) <9 :
        invalid=True
        flash("Please put at least 8 characters")
    if reg_password != reg_password_conf:
        invalid=True
        flash ("Password doesn't match")
    if invalid:
        return redirect ('/')
    else:
        hash= bcrypt.generate_password_hash(reg_password)
        query="INSERT INTO users (first_name,last_name,email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
        data= {
            'first_name': first_name,
            'last_name': last_name,
            "email": email,
            "password": hash
        }
        session['user_id']= mysql.query_db(query, data)
        return redirect('/wall')

@app.route('/wall')
def viewMain():
    query_msg= "SELECT users.first_name, users.last_name, messages.message, messages.in, messages.created_at FROM users JOIN messages ON users.id= messages.user_id"
    messages = mysql.query_db(query_msg)

    query_com= "SELECT users.first_name, users.last_name, comments.comment, comments.created_at, comments.message_id FROM users JOIN comments ON users.id= comments.user_id"
    comments = mysql.query_db(query_com)
    return render_template('wall.html', messages = messages, comments= comments)

@app.route('/post_msg', methods= ['POST'])
def post_msg():
    query = "INSERT INTO messages(message, created_at, updated_at, user_id) VALUES (:message, NOW(), NOW(), :user_id)"
    data = {
        'message': request.form['message'],
        'user_id': session['user_id']
    }
    mysql.query_db(query,data)
    return redirect ('/wall')


@app.route('/post_com/<message_id>', methods= ['POST'])
def post_com(message_id):
    comment= request.form['comment']
    query= "INSERT INTO comments(comment, created_at, updated_at, user_id, message_id) VALUES (:comment, NOW(), NOW(), :user_id, :message_id)"
    data = {
        'comment': comment,
        'user_id': session['user_id'],
        'message_id':message_id
    }
    mysql.query_db(query,data)
    return redirect ('/wall')

@app.route('/logout', methods= ['POST'])
def logout():
    return redirect ('/')


app.run(debug=True)
