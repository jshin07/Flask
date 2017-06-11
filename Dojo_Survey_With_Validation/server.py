from flask import Flask, render_template, redirect, request, session, flash

app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def process():
    name=request.form["name"]
    location=request.form["location"]
    language=request.form["language"]
    comment=request.form["comment"]

    if len(request.form['name'])<1:
        flash("Name cannot be empty!")
        return redirect ('/')
    elif len(request.form['comment'])<1:
        flash("Pleaes leave us comment. Cannot be empty!")
        return redirect ('/')
    elif len(request.form['comment'])>120:
        flash("Too long! Keep it under 120 characters ")
        return redirect ('/')

    else:
        return render_template('/results.html', name=name, location=location, language=language,comment=comment)


app.run(debug=True)
