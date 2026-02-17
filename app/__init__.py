from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__, template_folder="views")
    app.config.from_object(Config)

    # Import blueprints
    from app.controllers.auth_controller import auth_bp
    from app.controllers.course_controller import course_bp
    from app.controllers.admin_controller import admin_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(course_bp)
    app.register_blueprint(admin_bp)

    return app
