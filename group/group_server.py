from flask import Flask, render_template
app=Flask(__name__)
@app.route('/')
def rooms ():
    return render_template ("main.html")

@app.route('/dinner')
def dinner():
    return render_template ("dinner.html")


@app.route('/cheese')
def cheese():
    return render_template ("cheese.html")


@app.route('/red')
def red():
    return render_template ("red.html")

@app.route('/white')
def white():
    return render_template ("white.html")

@app.route('/steak')
def steak():
    return render_template ("steak.html")

@app.route('/wine')
def wine():
    return render_template ("wine.html")

@app.route('/rare')
def rare():
    return render_template ("rare.html")

@app.route('/medium')
def medium():
    return render_template ("medium.html")

@app.route('/welldone')
def welldone():
    return render_template ("welldone.html")

@app.route('/no')
def no():
    return render_template ("no.html")


app.run(host='192.168.1.13', port=5000, debug=True)
