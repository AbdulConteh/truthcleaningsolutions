import re 
from flask import flash 
from flask_app.config.mysqlconnection import connectToMySQL
db = "universal_flavors_db"

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
    def get_users(cls):
        query = "SELECT * FROM users;"
        users = []
        result = connectToMySQL(db).query_db(query)
        for user in result:
            users.append(cls(user))
        return users
