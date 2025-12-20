# apps/addition/routes.py - 11 (additon route)

from . import addition_bp
from flask import render_template

@addition_bp.route("/addition")
def index():
    return render_template("addition/view.html", title="Addition - Flask Blueprint")
