# app.py
# Import the application factory from core
from core.app_factory import create_app

# -----------------------------
# Create the Flask app
# -----------------------------
# create_app() returns a fully configured Flask app with:
# - registered blueprints (modules like books, categories)
# - global error handlers (404, 500)
# - authentication and middleware
app = create_app()

# -----------------------------
# Main entry point
# -----------------------------
# Run the app if this file is executed directly.
# 'debug=True' enables hot reload and better error messages in development.
if __name__ == "__main__":
    app.run(debug=True)
