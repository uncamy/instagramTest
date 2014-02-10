import os
import sqlite3
import string

from flask import Flask, request, session, g, redirect, url_for, \
                  abort, render_template, flash, json

DEBUG = True
API_KEY ='./api_key.txt'
app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/dietican', methods = ['GET', 'POST'])
def foo():
    return render_template('dietican.html')

@app.route('/about', methods = ['GET', 'POST'])
def bar():
    return render_template('about.html')

@app.route('/signin', methods= ['GET', 'POST'])
def signin():
    return render_template('test.html')

@app.route('/contact', methods= ['GET', 'POST'])
def contact():
    return render_template('test.html')

if __name__ == '__main__':
    app.run()
