# app/__init__.py

from flask import Flask

def create_app():
    app = Flask(__name__, template_folder='templates')  # Specify the templates folder if needed

    # You can add more configurations here if needed
    
    return app
