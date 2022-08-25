import re 
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
db = "universal_flavors_db"

class Reviews:
    def __init__(self, data):
        self.id = data['id']
        self.review = data['review']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod 
    def get_reviews(cls):
        query = "SELECT * FROM reviews WHERE id = %(id)s;"
        results = connectToMySQL(db).query_db(query)
        get_review = []
        for get in results:
            get_review.append (cls (get))
        return get_review

    def add_review(cls, data):
        query = """
        INSERT INTO reviews (review, user_id)
        VALUES ( %(review)s, %(user_id)s);
        """
        results = connectToMySQL(db).query_db(query, data)
        return results

    def update_reviews(cls, data, id):
        query = """
        UPDATE reviews SET review = %(review)s, updated_at = NOW() WHERE id = {id};
        """
        results = connectToMySQL(db).query_db(query, data)
        return results

