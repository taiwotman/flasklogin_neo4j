"""Initialize app."""
from flask import Flask
from .flask_py2neo import Py2Neo

from flask_login import LoginManager
db = Py2Neo()
login_manager = LoginManager()



def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)

    # Application Configuration
    app.config.from_object('config.Config')

    # Initialize Plugins
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        # Import parts of our application
        from . import routes
        from . import auth


        # Register Blueprints
        app.register_blueprint(routes.main_bp)
        app.register_blueprint(auth.auth_bp)

        # # Create unique index constraint
        try:
            db.graph.schema.create_uniqueness_constraint("User", "email")
        except:
            pass

        return app