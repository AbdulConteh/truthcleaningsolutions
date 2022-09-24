from flask_app import app 
from flask_app.models.reviews_model import Reviews
from flask import redirect, render_template, request, session, flash

@app.route('/reviews', methods=['POST'])
def reviews():
    data = {
        "review" : request.form['review']
    }
    id = Reviews.add_review(data)
    session['user_id'] = id
    return redirect ('/view_item')