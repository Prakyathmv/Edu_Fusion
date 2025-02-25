from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from bson.json_util import dumps
from models import SearchHistory, Reminder, mongo
from services import UserService

routes = Blueprint("routes", __name__)

@routes.route("/register", methods=["POST"])
def register():
    return UserService.register(request.json)

@routes.route("/login", methods=["POST"])
def login():
    return UserService.login(request.json)

@routes.route("/search", methods=["POST"])
@jwt_required()
def search():
    data = request.json
    user_id = get_jwt_identity()
    query = data.get("query")
    
    response = {"result": f"You searched for: {query}"}
    SearchHistory.save(user_id, query)
    return jsonify(response)

@routes.route("/search-history", methods=["GET"])
@jwt_required()
def get_search_history():
    user_id = get_jwt_identity()
    history = SearchHistory.get(user_id)
    return dumps(history)

@routes.route("/set-reminder", methods=["POST"])
@jwt_required()
def set_reminder():
    data = request.json
    user_id = get_jwt_identity()
    reminder_text = data.get("reminder_text")
    due_date = data.get("due_date")
    
    Reminder.save(user_id, reminder_text, due_date)
    return jsonify({"message": "Reminder set successfully!"})

@routes.route("/get-reminders", methods=["GET"])
@jwt_required()
def get_reminders():
    user_id = get_jwt_identity()
    reminders = Reminder.get(user_id)
    return dumps(reminders)

