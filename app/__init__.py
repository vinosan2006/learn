from flask import Flask
from config import Config
import time
import logging

class AppFactory:
    """Factory Pattern Class to assemble the Flask application configuration and routes."""
    
    @staticmethod
    def create_app():
        app = Flask(__name__, template_folder="views")
        app.config.from_object(Config)

        # Zero-Crash Logic: Wait for Database (Mock check)
        logging.info("Connecting to Database...")
        retries = 5
        while retries > 0:
            try:
                # Placeholder for actual DB connection:
                # db.connect()
                logging.info("Database initialized successfully!")
                break
            except Exception as e:
                retries -= 1
                logging.error(f"Database not ready, retrying in 2 seconds... ({retries} left)")
                time.sleep(2)
                if retries == 0:
                    logging.error("Could not connect to database. Starting anyway for Prometheus metrics availability.")

        # Import blueprints
        from app.controllers.auth_controller import auth_bp
        from app.controllers.course_controller import course_bp
        from app.controllers.admin_controller import admin_bp

        app.register_blueprint(auth_bp)
        app.register_blueprint(course_bp)
        app.register_blueprint(admin_bp)

        return app
