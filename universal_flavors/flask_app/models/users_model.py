import re 
from flask import flash 
from flask_app.config.mysqlconnection import connectToMySQL
db = "universal_flavors_db"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Users:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.address = data['address']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def add_user(cls, data):
        query = """
            INSERT INTO users (first_name, last_name, email, password)
            VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s);
        """
        results = connectToMySQL(db).query_db(query, data)
        return results

    def get_users(cls):
        query = "SELECT * FROM users;"
        users = []
        result = connectToMySQL(db).query_db(query)
        for user in result:
            users.append(cls(user))
        return users

    def edit_user(cls, data):
        query = """
            UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, address = %(address)s,
            updated_at = NOW() WHERE id = {id};
        """
        results = connectToMySQL(db).query_db(query, data)
        return results

    def login(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL(db).query_db(query, data)
        if len(results) < 1:
            return False
        return Users(results[0])

    @staticmethod
    def validate_users(Users):
        specialSym = ["$", "%", "@", "!", "&"]
        is_valid = True
        if len(Users['first_name']) < 3:
            flash("First name must be more than 3 letters! Please try again!", 'register')
            is_valid = False 
        if len(Users['last_name']) < 3:
            flash("Last name must be more than 3 letters! Please try again!", 'register')
            is_valid = False 
        if not EMAIL_REGEX.match(Users['email']):
            flash("Email must be registered! Please try again!", 'register')
            is_valid = False 
        if len(Users['password']) < 6:
            flash("Password must be more than 6 characters. Please try again!", 'register')
            is_valid = False 
        if not any(char.isdigit() for char in Users['password']):
            flash("Password must have at least 1 number. Please try again!", 'register')
            is_valid = False 
        if not any(char in specialSym for char in Users['password']):
            flash("Password should have at least 1 symbol! Please try again!", 'register')
            is_valid = False 
        if Users['password'] != Users['confirm_pw']:
            flash("Passwords don't match. Please try again!", 'login')
            is_valid = False 
        return is_valid

