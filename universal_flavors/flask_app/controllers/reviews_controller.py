from flask_app import app 
from flask_app.models.users_model import Users
from flask_app.models.reviews_model import Reviews
from flask import redirect, render_template, request, session, flash

@app.route('/reviews', methods=['POST'])
def reviews():
    data = {
        "reviews" : request.form['reviews']
    }
    Reviews.add_review(data)
    return redirect("/view_item")