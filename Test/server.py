from flask import Flask, render_template, redirect, request, session, flash

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
@app.route('/')
def index():
    return render_template('index.html')
#
# @app.route('/process', methods=['POST'])
# def process():
#     if len(request.form['name'])< 1:
#         flash("Name cannot be empty!")
#     else:
#         flash("Success! Your name is {}".format(request.form['name']))
#     return redirect('/')

@app.route('/process', methods=['POST'])
def process():
    if len(request.form['email'])< 1:
        flash("Name cannot be empty!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email!")
    else:
        flash("Success!")
    return redirect('/')


app.run(debug=True)
