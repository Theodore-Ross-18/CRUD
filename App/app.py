# CRUD REST API: Application

# Importing: Modules
import os # Environment Variables
from flask import Flask, Blueprint, render_template, request, jsonify # Web Handling
from flask_sqlalchemy import SQLAlchemy # Database Interactions

# Initializing: Flask App
app = Flask(__name__)

# Configure: Database URI (Settings)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'mysql+pymysql://flask_user:flask_password@localhost/flask_db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'supersecretkey'  # Required for flash messages

# Initialize: SQLAlchemy (app)
db = SQLAlchemy(app)

# DB: User Model
class User(db.Model):
    __tablename__ = 'users' # Table Name
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Create: tables in the DB (If: Not exist)
with app.app_context():
    db.create_all()

# Main Routes: Blueprint
main = Blueprint('main', __name__)

# Testing: Simple Route
@main.route('/')
def bonjour():
    return 'Bonjour le monde'

# Route: Show Users
@main.route('/users')
def show_users():
    users = User.query.all()
    return render_template('users.html', users=users)

# Route: CREATE
@main.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    if not username or not email:
        return jsonify({'error': 'Username and email are required!'}), 400

    if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
        return jsonify({'error': 'Username or email already exists!'}), 400

    new_user = User(username=username, email=email)
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully!', 'user': {'id': new_user.id, 'username': new_user.username, 'email': new_user.email}}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Error creating user: {str(e)}'}), 500

# Route: UPDATE
@main.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    if not username or not email:
        return jsonify({'error': 'Username and email are required!'}), 400

    if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
        return jsonify({'error': 'Username or email already exists!'}), 400

    new_user = User(username=username, email=email)
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully!', 'user': {'id': new_user.id, 'username': new_user.username, 'email': new_user.email}}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Error creating user: {str(e)}'}), 500

# Route: DELETE
@main.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    try:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Error deleting user: {str(e)}'}), 500

# Register: Blueprint
app.register_blueprint(main)

# Error Handlers: 404, 500
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

# Run: Flask Application
if __name__=='__main__':
    app.run(debug=True)