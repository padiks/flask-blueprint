# apps/home/routes.py [f]
# ------------------------
# Route definitions for the 'home' blueprint.
# Each route corresponds to a URL endpoint handled by the home blueprint.
# Templates are rendered from apps/home/templates/.

from . import home_bp
from flask import render_template

# ------------------------
# Home Page Route
# ------------------------
@home_bp.route("/")
def index():
    """
    Render the home page of the application.

    URL:
        GET /

    Returns:
        str: Rendered HTML page from 'apps/home/templates/home/view.html'.

    Template Context:
        title (str): Title of the page to display in the browser tab or header.
    """
    # Render the 'view.html' template located in apps/home/templates/home/
    # Pass the title variable to be used in the template
    return render_template("home/view.html", title="Home - Flask Blueprint")
