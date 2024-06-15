""" 

"""

# IMPORTS
from src import app
from flask import render_template


# Homepage
@app.route("/")
def home():
    return render_template("home.html")
