from flask_app import app 
from flask import Flask 
from flask import redirect, render_template, request, session 

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/view_item')
def view_items():
    return render_template('view_item.html')

@app.route('/login_and_reg')
def login_and_reg():
    return render_template('login_and_reg.html')