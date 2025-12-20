# core/errors.py - 4 (global errors)

from flask import render_template

def register_errors(app):

    @app.errorhandler(404)
    def not_found(error):
        return render_template("404.html"), 404
