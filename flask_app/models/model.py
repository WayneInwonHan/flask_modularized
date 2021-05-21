from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app

class User():

    def __init__(self, data):
        self.id = data['id']