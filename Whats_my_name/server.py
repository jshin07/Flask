from flask import Flask, render_template, request, redirect
app=Flask(__name__)
@app.route('/')
def main():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def creatname():
    print request.form['name']
    return redirect('/')


app.run(debug=True)
