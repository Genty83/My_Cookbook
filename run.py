"""
Main runnale file: This file is the main file for running the flask appliction
"""

# IMPORTS
import os 
from src import app

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )