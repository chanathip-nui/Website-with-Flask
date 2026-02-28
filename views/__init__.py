from .main import main_bp
from .accounts import accounts_bp


def register_blueprint(app):
    """Initializes the blueprints for the application."""
    app.register_blueprint(main_bp)
    app.register_blueprint(accounts_bp, url_prefix="/accounts")
