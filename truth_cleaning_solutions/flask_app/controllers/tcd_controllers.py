from flask_app import app
from flask import render_template, request

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about_us():
    return render_template("about_us.html")

@app.route("/how_we_clean")
def how_we_clean():
    return render_template("how_we_clean.html")

@app.route("/services")
def services():
    return render_template("our_services.html")

@app.route("/specialty_cleans")
def special_cleans():
    return render_template("specialty_clean.html")

