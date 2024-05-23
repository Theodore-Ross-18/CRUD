# CRUD REST API: Application

# Importing: Modules
import os # Environment Variables
from flask import Flask, Blueprint, render_template # Web Handling
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