# apps/__init__.py
from flask import Flask

def create_app():
    """
    Application factory function.
    Creates and configures the Flask app instance.
    Returns the Flask app object.
    """
    app = Flask(__name__, template_folder="../templates", static_folder="../static")

    # Register blueprints
    from apps.primer.routes import primer_bp
    app.register_blueprint(primer_bp, url_prefix='/')  # You can set other URL prefixes for other blueprints

    # Add more blueprints as needed
    # from apps.<other_module>.routes import <other_module_bp>
    # app.register_blueprint(<other_module_bp>, url_prefix='/<other_module_prefix>')

    # Return the configured Flask app
    return app
