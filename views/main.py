from flask import Blueprint, render_template
from flask_login import login_required

from acl import roles_required

# Define the blueprint for the main part of the site
main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    return render_template("index.html")


@main_bp.route("/admin")
@login_required
@roles_required("admin")
def admin_dashboard():
    return render_template("admin_dashboard.html")


@main_bp.route("/games")
def games():
    return "This is the games page."
