import os
import sqlite3
import string

from flask import Flask, request, session, g, redirect, url_for, \
                  abort, render_template, flash, json
from flask.ext.sqlalchemy import SQLAlchemy


DEBUG = True
API_KEY ='./api_key.txt'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)
USERNAME = 'admin'
PASSWORD = 'default'

@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/dietican', methods = ['GET', 'POST'])
def foo():
    return render_template('dietican.html')

@app.route('/about', methods = ['GET', 'POST'])
def bar():
    return render_template('about.html')

@app.route('/login', methods= ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['email'] != app.config['EMAIL']:
            error = 'Invalid email'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You are logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/contact', methods= ['GET', 'POST'])
def contact():
    return render_template('test.html')

if __name__ == '__main__':
    app.run()
