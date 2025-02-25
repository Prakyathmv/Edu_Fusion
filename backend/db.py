from flask_pymongo import PyMongo

mongo = PyMongo()  

def init_db(app):
    mongo.init_app(app)  
    try:
        mongo.db.command("ping")
        print("✅ MongoDB connection successful!")
    except Exception as e:
        print(f"❌ MongoDB connection failed: {e}")