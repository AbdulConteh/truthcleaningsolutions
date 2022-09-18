from flask_app import app 
from flask_bcrypt import Bcrypt
from flask import flash
from flask_app.models.users_model import Users
from flask import redirect, render_template, request, session 
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/view_item')
def view_items():
    return render_template('view_item.html')

@app.route('/login_and_reg')
def login_and_reg():
    return render_template('login_and_reg.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/register', methods=['POST'])
def register():
    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email" : request.form['email'],
        "password" : request.form['password'],
    }
    user = Users.add_user(data)
    print(user)
    session['user_id'] = user
    return redirect('/', user = user)

@app.route('/login', methods=['POST'])
def login():
    data = {
        "email" : request.form['email']
    }
    get_user = Users.login(data)
    print(get_user)
    if not get_user:
        flash("Unregistered email. Please try again!")
        return redirect('/')
    if not bcrypt.check_password_hash(get_user.password, request.form['password']):
        flash("Invalid password.")
        return redirect('/')
    session['user_id'] = get_user.id
    return redirect('/', get_user = get_user)