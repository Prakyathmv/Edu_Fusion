from datetime import datetime
from flask_pymongo import PyMongo

mongo = None  

class SearchHistory:
    @staticmethod
    def save(user_id, query):
        mongo.db.search_history.insert_one({
            "user_id": user_id,
            "query": query,
            "timestamp": datetime.utcnow()
        })
    
    @staticmethod
    def get(user_id):
        return mongo.db.search_history.find({"user_id": user_id})

class Reminder:
    @staticmethod
    def save(user_id, reminder_text, due_date):
        mongo.db.reminders.insert_one({
            "user_id": user_id,
            "reminder_text": reminder_text,
            "due_date": due_date,
            "created_at": datetime.utcnow()
        })
    
    @staticmethod
    def get(user_id):
        return mongo.db.reminders.find({"user_id": user_id})

