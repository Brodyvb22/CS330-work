#!/usr/bin/env python3
"""
Geography query data retrieval

@author:
@version: 2025.11
"""

from functools import cache
import sqlite3

from flask import current_app


@cache
def get_data_from_db(query: str, params: tuple | None = None) -> list:
    """Retrieve data from the database

    :param query: parametrized query to execute
    :param params: query parameters
    """
    db_file = current_app.config["DB_FILE"]

    conn = sqlite3.connect(db_file)
    conn.row_factory = sqlite3.Row 
    cur = conn.cursor()

    if params:
        cur.execute(query, params)
    else:
        cur.execute(query)

    results = cur.fetchall()
    conn.close()
    return results
