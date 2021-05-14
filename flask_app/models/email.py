from logging import StrFormatStyle
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Email:
    def __init__(self,data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def submit(self,data):
        query = "INSERT INTO emails(email,created_at,updated_at) \
        VALUES(%(email)s,NOW(),NOW());"
        return connectToMySQL('email_schema').query_db(query,data)
    
    @classmethod
    def show_all(cls):
        query = "SELECT * FROM emails;"
        return connectToMySQL('email_schema').query_db(query)

    @classmethod
    def show(cls,data):
        query = "SELECT * FROM emails WHERE id = %(emailid)s;"
        results = connectToMySQL('email_schema').query_db(query,data)
        return cls(results[0])
    
    @classmethod
    def delete(cls,data):
        query = "DELETE FROM emails WHERE emails.id = %(emailid)s;"
        return connectToMySQL('email_schema').query_db(query,data)