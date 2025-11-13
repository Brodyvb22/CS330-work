#!/usr/bin/env python3
"""
jokes api logic

@author:
@version: 2025.11
"""
import os
import pathlib
import random
import tomllib
from functools import cache

import pyjokes
from pyjokes.exc import CategoryNotFoundError, LanguageNotFoundError

from .models import Joke



class Joker:
    """
    A layer to retrieve jokes from the pyjokes package

    :raises ValueError: the dataset has not been initialized
    :raises ValueError: the language is invalid
    :raises ValueError: the category is invalid
    :raises ValueError: the joke id is invalid
    :raises ValueError: requested number of jokes is below 0
    """
    _dataset: list[Joke] = []

    @classmethod
    def init_dataset(cls):
        """
        Initialize the dataset

        Load jokes from the `pyjokes` package into a list of jokes
        """
        # TODO: Implement this method

        CONFIG_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.toml")
        with open(CONFIG_PATH, "rb") as f:
            languages = tomllib.load(f)["LANGUAGES"]


        cls._dataset = []
        for lang in languages.keys():
            for cat in ["neutral", "chuck"]:
                try:
                    jokes = pyjokes.get_jokes(language=lang, category=cat)
                    for text in jokes:
                        cls._dataset.append(Joke(language=lang, category=cat, text=text))
                except CategoryNotFoundError:
                    pass

    @classmethod
    def get_jokes(cls, language: str = "any", category: str = "any", number: int = 0) -> list[Joke]:
        """Get all jokes in the specified language/category combination

        :param language: language of the joke
        :param category: category of the joke
        :param number: number of jokes to return, 0 to return all
        """
        # TODO: Implement this method

        filtered = [
            joke for joke in cls._dataset
            if (language == "any" or joke.language == language)
            and (category == "any" or joke.category == category)
        ]

        if number == 0 or number >= len(filtered):
            return filtered

        return random.sample(filtered, number)

    @classmethod
    def get_the_joke(cls, joke_id: int) -> Joke:
        """Get a specific joke by id

        :param joke_id: joke id
        """
        # TODO: Implement this method
        if joke_id < 0 or joke_id >= len(cls._dataset):
            raise ValueError(f"Joke {joke_id} not found, try an id between 0 and {len(cls._dataset)-1}")

        return cls._dataset[joke_id]
