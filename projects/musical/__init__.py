# __init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET', 'dev-secret')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///musical.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static', 'covers')
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    db.init_app(app)

    from edit.routes import edit_bp
    from view.routes import view_bp
    from routes import main_bp

    app.register_blueprint(main_bp)      
    app.register_blueprint(edit_bp)      
    app.register_blueprint(view_bp)      

    with app.app_context():
        db.create_all()

    return app
