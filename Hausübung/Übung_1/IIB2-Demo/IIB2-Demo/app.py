"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""
from flask import Flask, render_template, request, flash, session, redirect, url_for
#from werkzeug.security import generate_password_hash, check_password_hash
import auth
import application

def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="dev")
    @app.route("/hello")
    def hello():
        return "Hello, World!"

    # apply the blueprints to the app
    app.register_blueprint(auth.bp)
    app.register_blueprint(application.bp)
    return app

if __name__ == '__main__':   
	app = create_app()
	app.run(host = '0.0.0.0',port=8090)

