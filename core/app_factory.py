# core/app_factory.py - 3 (application factory)
from flask import Flask
from config import Config
from pathlib import Path

def create_app():
    # Ensure paths are absolute so Flask always finds templates
    base_dir = Path(__file__).resolve().parent.parent  # project root

    app = Flask(
        __name__,
        template_folder=str(base_dir / "templates"),
        static_folder=str(base_dir / "static")
    )

    app.config.from_object(Config)

    # Register blueprints
    from apps.home import home_bp
    app.register_blueprint(home_bp, url_prefix="/")
    
    from apps.addition import addition_bp                 # 13 Register the blueprint in core/app_factory.py
    app.register_blueprint(addition_bp, url_prefix="/")   # 13 Register the blueprint in core/app_factory.py

    # Register global error handlers
    from core.errors import register_errors
    register_errors(app)

    return app
