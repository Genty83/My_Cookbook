"""
This file contains all the SQLAlchemy models
for the database.
"""

# IMPORTS
from src import db


# Accounts model
class Accounts(db.Model):
    """ Database model for user accounts """

    # properties for db columns
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(50), nullable = False)
    last_name = db.Column(db.String(50), nullable = False)
    username = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), nullable = False)
    password = db.Column(db.String(100), nullable = False)
    user = db.relationship("RecipeOverview", backref="accounts", cascade="all, delete")
    

    # Repo method
    def __repr__(self):
        """ Reproduces a string of the object """
        return f"{self.username}"


# Recipe Overview Model
class RecipeOverview(db.Model):
    """ Database model class for the recipe overview table """

    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db,Text(), nullable = False)
    date_added = db.Column(db.Date(), nullable = False)
    rating = db.Column(db.Float, nullable = False)
    cook_time = db.Column(db.Integer, nullable = False)
    prep_time = db.Column(db.Integer, nullable = False)
    servings = db.Column(db.Integer, nullable = False)
    recipe_type = db.Column(db.String(100), nullable = False)
    user_id = db.Column(db.ForeignKey("accounts.id"), ondelete="CASCADE", nullable = False)


     # Repo method
    def __repr__(self):
        """ Reproduces a string of the object """
        return f"{self.description}"