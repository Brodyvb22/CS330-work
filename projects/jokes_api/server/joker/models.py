#!/usr/bin/env python3
"""
jokes api models

@author:
@version: 2025.11
"""

from dataclasses import dataclass


class Joke:
    """
    A model to store individual jokes

    Each joke has language, category, and text
    """

    # TODO: Implement this class
    def __init__(self, language: str, category: str, text: str):
        self.language = language
        self.category = category
        self.text = text
##DONE