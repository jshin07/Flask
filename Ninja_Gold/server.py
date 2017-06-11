import random
from flask import Flask, render_template, request, redirect, session

app=Flask(__name__)
app.secret_key='ThisIsSecret'

@app.route('/')
def main():
    session['count'] =0
    session['message'] =" "

    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process():
    if request.form['building'] == "farm":
        farmCount = random.randint(10,20)
        session['count'] += farmCount
        msg = "Earned "+ str(farmCount)+ " golds from the farm!"

    elif request.form['building'] == "cave":
        caveCount = random.randint(5,11)
        session['count'] += caveCount
        msg = "Earned "+ str(caveCount)+ " golds from the cave!"

    elif request.form['building'] == "house":
        houseCount = random.randint(2,5)
        session['count'] += houseCount
        msg = "Earned "+ str(houseCount)+ " golds from the house!"

    elif request.form['building'] == "casino":
        casinoCount = random.randint(-50,50)
        if casinoCount >0:
            session['count'] += casinoCount
            msg = "Earned "+ str(casinoCount)+ " golds from the casino!"
            # print msg
        else:
            session['count'] += casinoCount
            msg = "Lost "+ str(casinoCount)+ " golds from the casino! Ouch!"
            # print msg

    session['message'] += msg +"\n" +"\t"
    # print session['message']

    return render_template('index.html')

app.run(debug=True)
