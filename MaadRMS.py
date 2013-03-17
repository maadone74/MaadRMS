# MaadRMS -- Open Source Restaurant Management System
# Created by: Maadworks Software
from flask import Flask, session, request, url_for, redirect
from flask.templating import render_template
import pymongo

app = Flask(__name__)

# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

##
# Supporting Functions
##

def valid_login(username, pass1, pass2):
    """Validates if the username and passwords are in proper
    formats. It also checks if the user is in the database
    and passwords match"""
   # return False
    if pass1 != pass2:
        return False
    mongoConnection = pymongo.MongoClient()
    MaadRMSDb = mongoConnection.MaadRMS
    usersCollection = MaadRMSDb.users
    userDoc = usersCollection.find_one({"username" : username})
    if userDoc is None:
        return False
    if userDoc['passwd'] != pass1:
        return False
    session['username'] = username
    return True


def login_the_user(username):
    """Setups the user for a session"""
    return render_template('main_menu_tpl.html')

#
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

@app.route('logout')
def get_logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('get_home'))


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
    app.run(host="0.0.0.0", port=8080)
