# apps/addition/__init__.py [h]
# -----------------------------
# Blueprint definition for the 'addition' module.
# This module creates the 'addition' blueprint which organizes all
# routes, templates, and static files related to the addition section of the app.

from flask import Blueprint

# ------------------------
# Step 1: Create the blueprint
# ------------------------
addition_bp = Blueprint(
    "addition",              # Blueprint name used to register and reference it
    __name__,                # Package name (__name__) for locating resources
    template_folder="templates"  # Look for HTML templates in apps/addition/templates
    # static_folder can be added here if addition has its own static files
)

# ------------------------
# Step 2: Import the routes
# ------------------------
# This imports the route definitions associated with this blueprint.
# Routes should be defined in apps/addition/routes.py
from . import routes
