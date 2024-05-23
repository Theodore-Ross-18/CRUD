# CRUD REST API: Application

# Importing: Modules
import os # Environment Variables
from flask import Flask # Web Handling
from flask_sqlalchemy import SQLAlchemy # Database Interactions

# Initializing: Flask App
app = Flask(__name__)

# Configure: Database URI (Settings)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'mysql+pymysql://flask_user:flask_password@localhost/flask_db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'supersecretkey'  # Required for flash messages

# Initialize: SQLAlchemy (app)
db = SQLAlchemy(app)