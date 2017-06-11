from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)
app.secret_key='ThisIsSecret'

@app.route('/')
def main():
    try:
        session['count'] += 1
    except KeyError:
        session['count'] = 1

    return render_template('index.html')

@app.route('/addtwo', methods=['POST'])
def addtwo():
    session['count'] += 1
    return redirect('/')

@app.route('/refresh', methods=['POST'])
def refresh():
    session['count'] =0
    return redirect('/')


app.run(debug=True)
