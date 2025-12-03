from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(BASE_DIR, "musical.db")

    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "dev"

    db.init_app(app)


    from edit.routes import edit_bp
    from view.routes import view_bp
    from routes import main_bp


    app.register_blueprint(main_bp)
    app.register_blueprint(edit_bp, url_prefix="/edit")
    app.register_blueprint(view_bp, url_prefix="/view")

    @app.route("/")
    def index():
        return "<h1>Musical App Running</h1><p>Go to /edit or /view</p>"


    return app