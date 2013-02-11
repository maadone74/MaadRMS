# MaadRMS -- Open Source Restaurant Management System
# Created by: Maadworks Software
from flask import Flask, Session, request
from flask.templating import render_template

app = Flask(__name__)

##
# Supporting Functions
##

def valid_login(username, pass1, pass2):
    """Validates if the username and passwords are in proper
    formats"""
    return False

def login_the_user(username):
    """Looks for the user in the database"""
    pass

##
# routes
##

@app.route('/')
def get_home():
    return render_template('home_tpl.html')

@app.route('/login', methods=['POST','GET'])
def get_login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
            request.form['password1'], request.form['password2']):
            return login_the_user(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below this is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login_tpl.html', error=error)

@app.route('/kitchen')
def get_kitchen():
    return 'Kitchen Page'

@app.route('/servers')
def get_servers():
    return 'Server Pages'

@app.route('/bar')
def get_bar():
    return 'Bar Page'

@app.route('/admin')
def get_admin():
    return 'Admin Page'

@app.route('/manager')
def get_managers():
    return 'Manager\'s Page'

@app.route('/order')
def online_order():
    return 'Online Ordering'


if __name__ == '__main__':
    app.run()
