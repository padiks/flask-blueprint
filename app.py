# app.py [b]
# ------------------------
# Entry point for the Flask application.
# This file initializes the Flask app using the application factory pattern
# and starts the development server when executed directly.

from core.app_factory import create_app

# Create a Flask app instance using the factory function
app = create_app()

# Run the app only if this script is executed directly
if __name__ == "__main__":
    # Starts the Flask development server on default host (127.0.0.1) and port (5000)
    # Use 'debug=True' in config to enable hot reload and detailed error pages
    app.run()
