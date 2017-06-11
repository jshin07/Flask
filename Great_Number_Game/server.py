import random
from flask import Flask, render_template, request, redirect, session

app=Flask(__name__)
app.secret_key='ThisIsSecret'

@app.route('/')
def main():

    return render_template('index.html')


@app.route('/results', methods=['POST'])
def results():
    session["randomNum"] = random.randint(1,100)
    rand = session["randomNum"]
    print "The randomNum is ", rand

    session["yourguess"]= int(request.form["yourguess"])
    guess=session["yourguess"]
    print "Your guess is" , guess
    print guess< rand

    if int(guess) >100:
        session['result'] ="Error: Put number between 1-100"
    elif guess < rand:
        session['result'] ="Too low!"
    elif guess > rand:
        session['result'] ="Too high"
    elif guess == rand:
        session['result']="You won!"
    return render_template('index.html')

@app.route('/refresh', methods=['POST'])
def refresh():
    return redirect('/')



app.run(debug=True)
