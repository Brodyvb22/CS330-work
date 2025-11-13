#!/usr/bin/env python3
"""
jokes api routes

@author:
@version: 2025.11
"""

from typing import Literal

from flask import Blueprint, abort, jsonify, current_app
from werkzeug import Response
from werkzeug.exceptions import NotFound

from .logic import Joker

main = Blueprint("main", __name__, url_prefix="/api/v1/jokes")


@main.route("/<string:language>/<string:category>/all")
def get_all_jokes_by_language_and_category(language: str, category: str) -> Response:
    """Get all jokes in the specified language/category combination

    :param language: language of the joke
    :param category: category of the joke
    """
    # TODO: Implement this function
    try:
        jokes = current_app.joker.get_jokes(language, category)
        return jsonify({"jokes": [j.text for j in jokes]})
    except ValueError:
        abort(404, description=f"Language {language} or Category {category} not found")


@main.route("/<string:language>/<string:category>/<int:number>")
def get_n_jokes_by_language_and_category(language: str, category: str, number: int):
    """Get multiple jokes

    :param language: language of the jokes
    :param category: category of the jokes
    :param number: number of the jokes to return
    """
    # TODO: Implement this function
    try:
        jokes = current_app.joker.get_jokes(language, category, number)
        return jsonify({"jokes": [j.text for j in jokes]})
    except ValueError:
        abort(404, description=f"Language {language} or Category {category} not found")


@main.route("/<int:joke_id>")
def get_the_joke(joke_id: int):
    """Get a specific joke by id

    :param joke_id: joke id
    """
    # TODO: Implement this function
    try:
        joke = current_app.joker.get_the_joke(joke_id)
        return jsonify({"joke": joke.text})
    except ValueError as e:
        abort(404, description=str(e))


@main.errorhandler(404)
def not_found(error: NotFound) -> tuple[Response, Literal[404]]:
    # TODO: Implement this function
    return jsonify({"error": error.description if hasattr(error, "description") else "Not found"}), 404