from flask import Flask, render_template, redirect, request, session, flash

import re

app = Flask(__name__)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app.secret_key = 'secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    email=request.form['email']
    fn=request.form["fn"]
    ln=request.form["ln"]
    pw=request.form["pw"]
    conf_pw=request.form["conf_pw"]

    if len(email)<1 or len(fn)< 1 or len(ln) <1 or len(pw) <1 or len(conf_pw)<1:
        flash("All fields must be entered!")

    # elif not EMAIL_REGEX.match('email'):
    #     flash("Pleaes put a valid email")

    elif 'fn'.isdigit() == true:
        print "ok"
        # flash("Name cannot contain any numbers")

    # elif len(pw) < 9:
    #     flash("Password must be more than 8 characters")
    #
    # elif pw != conf_pw:
    #     flash("Check your password again")

    else:
        flash("Thank you for submitting your information")
        return redirect ('/')

app.run(debug=True)
