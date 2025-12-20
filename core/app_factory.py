# core/app_factory.py [c]
# ------------------------
# Application factory for the Flask project.
# This module creates and configures the Flask app instance.
# Responsibilities:
#   - Set template and static folders
#   - Load global configuration
#   - Register blueprints for modular components
#   - Set up global error handlers

from flask import Flask
from config import Config
from pathlib import Path

def create_app():
    """
    Factory function to create and configure a Flask application instance.

    Returns:
        Flask: Fully configured Flask app.

    Steps performed:
        1. Determine the absolute project root directory.
        2. Create a Flask app instance with template and static folders.
        3. Load global configuration from Config class.
        4. Register blueprints for modular components.
        5. Register global error handlers.
    """

    # ------------------------
    # Step 1: Determine the base directory
    # ------------------------
    # Resolve absolute path to the project root so Flask can reliably find templates and static files
    base_dir = Path(__file__).resolve().parent.parent  # project root

    # ------------------------
    # Step 2: Create Flask app instance
    # ------------------------
    app = Flask(
        __name__,
        template_folder=str(base_dir / "templates"),  # HTML templates directory
        static_folder=str(base_dir / "static")       # Static files directory (CSS, JS, images)
    )

    # ------------------------
    # Step 3: Load configuration
    # ------------------------
    # Load settings from the global Config class
    app.config.from_object(Config)

    # ------------------------
    # Step 4: Register blueprints
    # ------------------------
    # Blueprints organize the app into reusable modules
    from apps.home import home_bp
    app.register_blueprint(home_bp, url_prefix="/")  # Home blueprint at root URL

    from apps.addition import addition_bp
    app.register_blueprint(addition_bp, url_prefix="/")  # Addition blueprint at root URL

    # ------------------------
    # Step 5: Register global error handlers
    # ------------------------
    # Centralized error handling (404, 500, etc.)
    from core.errors import register_errors
    register_errors(app)

    # ------------------------
    # Step 6: Return app instance
    # ------------------------
    return app
