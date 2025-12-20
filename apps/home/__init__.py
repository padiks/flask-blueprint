# apps/home/__init__.py - 5 (blueprint definition)

from flask import Blueprint

home_bp = Blueprint(
    "home",
    __name__,
    template_folder="templates"  # looks inside apps/home/templates
)

from . import routes  # import the routes
