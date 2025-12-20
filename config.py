# config.py [a]
# ------------------------
# Global configuration file for the Flask application.
# Stores settings like secret keys, debug mode, and other global parameters.
# Any module or blueprint can access these settings through app.config

class Config:
    """
    Configuration class for Flask application.

    Attributes:
        SECRET_KEY (str): Used by Flask to secure sessions, cookies, and CSRF tokens.
        DEBUG (bool): Enables or disables Flask's debug mode.
    """

    # Secret key for session management and CSRF protection
    SECRET_KEY = "The quick brown fox jumps over the fence."

    # Enable debug mode for development
    DEBUG = True
