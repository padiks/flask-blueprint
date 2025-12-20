# apps/addition/__init__.py - 10 (blueprint definition)

from flask import Blueprint

addition_bp = Blueprint(
    "addition",
    __name__,
    template_folder="templates"  # looks inside apps/addition/templates
)

from . import routes  # import the routes
