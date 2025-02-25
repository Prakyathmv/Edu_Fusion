from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from config import Config
from routes import routes
from db import init_db, mongo  

app = Flask(__name__)
app.config.from_object(Config)

init_db(app) 
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

app.register_blueprint(routes)

if __name__ == "__main__":
    app.run(debug=True)
