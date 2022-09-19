from flask_app import app 
from flask_bcrypt import Bcrypt
from flask_app.models.users_model import Users
from flask_app.models.reviews_model import Reviews
from flask import redirect, render_template, request, session, flash
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

@app.route("/register", methods=['POST'])
def create():
    if not Users.validate_users(request.form):
        return redirect('/')
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
        "password" : bcrypt.generate_password_hash(request.form['password'])
    }
    # print(data['password'])
    id = Users.add_user(data)
    session['user_id'] = id
    return redirect ('/')

@app.route("/login", methods=['POST'])
def login():
    data = {
        "email" : request.form["email"]
    }
    user = Users.login(data)
    if not user:
        flash("Unregistered email. Please try again", "login")
        return redirect('/')
    if not bcrypt.check_password_hash(Users.password, request.form['password']):
        flash("Invalid password.", "login")
        return redirect('/')
    session['user_id'] = user.id
    return redirect ('/profile')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')