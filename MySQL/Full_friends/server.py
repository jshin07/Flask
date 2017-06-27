from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'full_friends')
@app.route('/')
def index():
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    return render_template('index.html', friends = friends )

@app.route('/add', methods=['POST'])
def create():
    query = "INSERT INTO friends(name, age, friends_since, created_at, updated_at) VALUES(:name, :age ,NOW(),NOW(), NOW())"
    data= {
        'name': request.form['name'],
        'age': request.form['age']
    }
    mysql.query_db(query,data)
    return redirect('/')

app.run(debug=True)
