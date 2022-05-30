from flask import Flask, flash, redirect, render_template, request, url_for, session
app = Flask(__name__)

# @app.route('/')
# def index():
#    if 'username' in session:
#       username = session['username']
#          return 'Logged in as ' + username + '<br>' + \
#          "<b><a href = '/logout'>click here to log out</a></b>"
#    return "You are not logged in <br><a href = '/login'></b>" + \
#       "click here to log in</b></a>

@app.route('/Login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))

# blm