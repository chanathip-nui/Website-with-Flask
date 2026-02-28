from flask import Blueprint, render_template
from flask_login import login_required
from acl import roles_required

# Define the blueprint for the main part of the site
main_bp = Blueprint("main", __name__)

# Dummy data so your UI grid renders successfully
dummy_item = {
    "name": "Sample Product",
    "category": "Entertainment",
    "rating": "4.5",
    "icon_url": "https://placehold.co/150x150",
}
dummy_list = [dummy_item] * 6


@main_bp.route("/")
def index():
    return render_template("main/index.html", apps=dummy_list)


@main_bp.route("/games")
def games():
    return render_template("main/games.html", games=dummy_list)


@main_bp.route("/movies")
def movies():
    return render_template("main/movies.html", movies=dummy_list)


@main_bp.route("/books")
def books():
    return render_template("main/books.html", books=dummy_list)


@main_bp.route("/admin")
@login_required
@roles_required("admin")
def admin_dashboard():
    return render_template("admin_dashboard.html")
