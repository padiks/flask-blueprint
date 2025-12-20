# apps/addition/routes.py [i]
# ----------------------------
# Route definitions for the 'addition' blueprint.
# Each route corresponds to a URL endpoint handled by the addition blueprint.
# Templates are rendered from apps/addition/templates/.

from . import addition_bp
from flask import render_template

# ------------------------
# Addition Page Route
# ------------------------
@addition_bp.route("/addition")
def index():
    """
    Render the addition page of the application.

    URL:
        GET /addition

    Returns:
        str: Rendered HTML page from 'apps/addition/templates/addition/view.html'.

    Template Context:
        title (str): Title of the page to display in the browser tab or header.
    """
    # Render the 'view.html' template located in apps/addition/templates/addition/
    # Pass the title variable to be used in the template
    return render_template("addition/view.html", title="Addition - Flask Blueprint")
