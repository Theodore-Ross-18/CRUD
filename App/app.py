# CRUD REST API: Application

# Importing: Modules
import os # Environment Variables
from flask import Flask # Web Handling
from flask_sqlalchemy import SQLAlchemy # Database Interactions

# Initializing: Flask App
app = Flask(__name__)