from flask_app import app
from flask_app.controllers import users_controller
from flask_app.controllers import reviews_controller 
from flask_app.controllers import customer_question_controller

if __name__ == "__main__":
    app.run(debug=True)