# Configurations: Application

# Importing: Modules
from flask import Flask # Instance of a Flask web application
from flask_restful import Api # Create RESTful APIs in Flask
from flask_sqlalchemy import SQLAlchemy # Database Interactions

# Instance: Flask class
app = Flask(__name__)

# Configures: URI for the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://your_username:your_password@localhost/flask_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Instance: SQLAlchemy and Api Class
db = SQLAlchemy(app)
api = Api(app)