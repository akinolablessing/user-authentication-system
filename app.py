from flask import Flask
from flask_jwt_extended import JWTManager
from auth.user_authentication_auth import auth_bp
from database.user_authentication_database import mongo
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
app.config['MONGO_URI'] = 'mongodb://localhost:27017/user-authentication-db'

mongo.init_app(app)
jwt = JWTManager(app)

app.register_blueprint(auth_bp)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)

