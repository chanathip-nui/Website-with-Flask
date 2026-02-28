from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user

from forms import LoginForm, RegisterForm
from models import db, User
from acl import roles_required

accounts_bp = Blueprint("accounts", __name__)
main_bp = Blueprint("main", __name__)


def register_blueprint(app):
    app.register_blueprint(accounts_bp, url_prefix="/accounts")
    app.register_blueprint(main_bp)


@main_bp.route("/")
def index():
    return render_template("index.html")


@main_bp.route("/admin")
@login_required
@roles_required("admin")
def admin_dashboard():
    return render_template("admin_dashboard.html")


@accounts_bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    form = RegisterForm()
    if form.validate_on_submit():
        existing_user = User.query.filter(
            (User.username == form.username.data) | (User.email == form.email.data)
        ).first()
        if existing_user:
            flash("Username or email already exists.")
            return redirect(url_for("accounts.register"))

        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
        )
        db.session.add(user)
        db.session.commit()
        flash("Registration successful. Please log in.")
        return redirect(url_for("accounts.login"))
    return render_template("accounts/register.html", form=form)


@accounts_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.verify_password(form.password.data):
            login_user(user)
            next_page = request.args.get("next")
            return redirect(next_page or url_for("main.index"))
        else:
            flash("Invalid username or password.")
    return render_template("accounts/login.html", form=form)


@accounts_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
