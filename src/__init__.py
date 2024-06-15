"""
This package contains all the files for creating the application.
This init file contains the main app and db variables for the flask application
and the sqlalchemy variable.
Both are initilized in this file.
"""

# IMPORTS
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env


# Create new app instance
app = Flask(__name__)
# Configure app
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
app.app_context().push()

# Create new database instance
db = SQLAlchemy(app)

# Import routes file last to avoid circular import
from src import routes