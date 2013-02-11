# MaadRMS -- Open Source Restaurant Management System
# Created by: Maadworks Software
from flask import Flask, Session
from flask.templating import render_template

app = Flask(__name__)


@app.route('/')
def get_home():
    return 'Welcome To MaadRMS'

@app.route('/login')
def get_login():
    return render_template('login_tpl.html')

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
