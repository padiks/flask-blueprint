# core/app_factory.py
import os
from flask import Flask, redirect, url_for

from config import Config

# Import blueprints (feature-based modules)
from apps.primer.routes import primer_bp

# Import core infrastructure
from core.errors import register_error_handlers

# -----------------------------
# Project root directory
# -----------------------------
BASE_DIR = os.path.abspath(
    os.path.dirname(os.path.dirname(__file__))
)

# -----------------------------
# Application Factory
# -----------------------------
def create_app():
    # Create Flask app with explicit template and static paths
    app = Flask(
        __name__,
        template_folder=os.path.join(BASE_DIR, "templates"),
        static_folder=os.path.join(BASE_DIR, "static"),
    )

    # Load configuration from config.py
    app.config.from_object(Config)

    # -------------------------
    # Root route
    # -------------------------
    # Redirect to primer.view instead of books
    @app.route("/")
    def index():
        return redirect(url_for("primer.view"))  # Adjusted to point to primer.view

    # -------------------------
    # Register blueprints
    # -------------------------
    # Register the primer blueprint only
    app.register_blueprint(primer_bp, url_prefix="/primer")

    # -------------------------
    # Register global infrastructure
    # -------------------------
    register_error_handlers(app)
    # Middleware registration removed

    return app
