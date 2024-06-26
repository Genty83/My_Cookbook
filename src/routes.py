""" 

"""

# IMPORTS
from src import app
from flask import render_template


# Homepage
@app.route("/")
def home():
    return render_template("pages/home.html")


# View Recipes 
@app.route("/view_recipes")
def view_recipes():
    return render_template("pages/view_recipes.html")


# Create Recipe
@app.route("/create_recipe")
def create_recipe():
    return render_template("pages/create_recipe.html")


# About
@app.route("/about")
def about():
    return render_template("pages/about.html")


# Accounts
@app.route("/accounts", methods=["GET", "POST"])
def accounts():
    return render_template("pages/accounts.html")