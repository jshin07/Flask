from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
mysql = MySQLConnector(app,'email_db')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app.secret_key = 'secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/email', methods=['POST'])
def validation():
    email=request.form['email']
    if not EMAIL_REGEX.match(email):
        flash ('Email is not valid')
        return redirect('/')
    else:
        session['email'] =email
        query= "INSERT INTO users(email,created_at,updated_at) VALUES ( :email, NOW(), NOW())"
        data= {'email': request.form ['email']}
        mysql.query_db(query,data)
        users=mysql.query_db(query,data)
        return redirect ('/success')

@app.route('/success')
def success():
    query= "SELECT * FROM users"
    users= mysql.query_db(query)
    return render_template('success.html', users= users)




app.run(debug=True)
