# core/errors.py [d]
# ------------------------
# Global error handlers for the Flask application.
# This module centralizes the handling of common HTTP errors
# so all blueprints and routes can use the same error pages.

from flask import render_template

def register_errors(app):
    """
    Register global error handlers for the Flask app.

    Args:
        app (Flask): The Flask application instance.

    Usage:
        from core.errors import register_errors
        register_errors(app)
    """

    # ------------------------
    # 404 Not Found Error Handler
    # ------------------------
    @app.errorhandler(404)
    def not_found(error):
        """
        Handle 404 errors (page not found).

        Args:
            error: The error object containing information about the 404.

        Returns:
            A rendered '404.html' template with HTTP status code 404.
        """
        # Render a custom 404 error page located in templates/404.html
        return render_template("404.html", title="Page not found - Flask Blueprint"), 404
