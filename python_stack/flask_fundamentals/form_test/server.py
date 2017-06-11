from flask import Flask, render_template, request, redirect
app= Flask (__name__)

# @app.route('/')
# def index():
#     return render_template("index.html")
#
# @app.route('/users', methods=["POST"])
# def create_user():
#     # print "Got Post Info"
#     name = request.form['name']
#     email = request.form ['email']
#     return render_template("success.html")
#     # return redirect('/')
#
# app.run(debug=True)
#
#
# @app.route('/user/<username>')
# def show_user_profile(username):
#     print username
#     return render_template("user.html")


@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
		print username
		print id
    return render_template ("user.html")


app.run(debug=True)
