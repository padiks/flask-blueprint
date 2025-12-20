# apps/home/__init__.py [e]
# ------------------------
# Blueprint definition for the 'home' module.
# This module creates the 'home' blueprint which organizes all
# routes, templates, and static files related to the home section of the app.

from flask import Blueprint

# ------------------------
# Step 1: Create the blueprint
# ------------------------
home_bp = Blueprint(
    "home",                 # Blueprint name used to register and reference it
    __name__,               # Package name (__name__) for locating resources
    template_folder="templates"  # Look for HTML templates in apps/home/templates
    # static_folder can be added here if home has its own static files
)

# ------------------------
# Step 2: Import the routes
# ------------------------
# This imports the route definitions associated with this blueprint.
# Routes should be defined in apps/home/routes.py
from . import routes
