#!/usr/bin/env python3
"""
Serving `pyjokes` via templates

@authors:
@version: 2024.10
"""

import random

import pyjokes
from flask import Flask, abort, render_template, request
from pyjokes.exc import PyjokesError

LANGUAGES = {
    "cs": "CZECH",
    "de": "GERMAN",
    "en": "ENGLISH",
    "es": "SPANISH",
    "eu": "BASQUE",
    "fr": "FRENCH",
    "gl": "GALICIAN",
    "hu": "HUNGARIAN",
    "it": "ITALIAN",
    "lt": "LITHUANIAN",
    "pl": "POLISH",
    "sv": "SWEDISH",
}

CATEGORIES = [
    "all", "neutral", "chuck"
]

app = Flask(__name__)


@app.get("/")
def index():
    """Render the template with form"""
    # TODO: Implement this function
    return render_template(
        "jokes.html",
        languages=LANGUAGES,
        categories=CATEGORIES,
        jokes=None,
        numbers=range(1,10)
    )


@app.post("/")
def index_jokes():
    """Render the template with jokes"""
    # TODO: Implement this function
    language = request.form.get("language", "en")
    category = request.form.get("category", "all")
    number = int(request.form.get("number", 1))

    jokes = get_jokes(language=language, category=category, number=number)

    return render_template(
        "jokes.html",
        languages=LANGUAGES,
        categories=CATEGORIES,
        numbers=range(1, 10),
        jokes=jokes,
    )



def get_jokes(
    language: str = "en",
    category: str = "all",
    number: int = 1,
) -> list[str]:
    """Return a list of jokes"""
    # TODO: Implement this function
    try:
        jokes_list = pyjokes.get_jokes(language=language, category=category)
    except PyjokesError:
        return ["No jokes available for this selection."]

    if number <= 1:
        return [random.choice(jokes_list)] if jokes_list else ["No jokes available."]
    
    return random.sample(jokes_list, min(number, len(jokes_list)))
