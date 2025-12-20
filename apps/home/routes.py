# apps/home/routes.py - 6 (home route)

from . import home_bp
from flask import render_template

@home_bp.route("/")
def index():
    return render_template("home/view.html", title="Home - Flask Blueprint")
