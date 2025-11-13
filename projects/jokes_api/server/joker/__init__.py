#!/usr/bin/env python3
"""
jokes api

@author:
@version: 2025.11
"""

import pathlib
import tomllib

from flask import Flask
from flask_cors import CORS

from .routes import main
from .logic import Joker


def create_app() -> Flask:
    this_app = Flask(__name__)

    # TODO: Implement this function

    # Enable CORS
    CORS(this_app)

    # Initialize Joker dataset
    Joker.init_dataset()
    this_app.joker = Joker  # attach to app for routes to use

    # Register blueprint
    this_app.register_blueprint(main)

    return this_app
