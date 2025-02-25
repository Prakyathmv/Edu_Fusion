from flask import jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token
from models import mongo

bcrypt = Bcrypt()

class UserService:
    @staticmethod
    def register(data):
        username = data.get("username")
        password = data.get("password")
        
        if mongo.db.users.find_one({"username": username}):
            return jsonify({"message": "Username already exists"}), 400
        
        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
        mongo.db.users.insert_one({"username": username, "password": hashed_password})
        return jsonify({"message": "User registered successfully"})

    @staticmethod
    def login(data):
        username = data.get("username")
        password = data.get("password")
        user = mongo.db.users.find_one({"username": username})
        
        if user and bcrypt.check_password_hash(user["password"], password):
            access_token = create_access_token(identity=username)
            return jsonify({"access_token": access_token})
        else:
            return jsonify({"message": "Invalid credentials"}), 401
