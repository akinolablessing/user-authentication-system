from flask import Blueprint, request, jsonify
from database.user_authentication_database import mongo
from utils.user_authentication_utils import generate_token
from bson.objectid import ObjectId
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    if not all([name, email, password]):
        return jsonify({'error': 'All fields are required'}), 400

    if mongo.db.users.find_one({"email": email}):
        return jsonify({'error': 'Email already registered'}), 400

    hashed_password = generate_password_hash(password)
    mongo.db.users.insert_one({"name": name, "email": email, "password": hashed_password})

    return jsonify({'message': 'User registered successfully'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = mongo.db.users.find_one({"email": email})
    if user and check_password_hash(user['password'], password):
        token = generate_token(str(user['_id']))
        return jsonify({'token': token}), 200

    return jsonify({'error': 'Invalid credentials'}), 401

@auth_bp.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    user_id = get_jwt_identity()
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})

    if user:
        return jsonify({
            'id': str(user['_id']),
            'name': user['name'],
            'email': user['email']
        }), 200
    return jsonify({'error': 'User not found'}), 404
