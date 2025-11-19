#!/usr/bin/env python3
"""
Geography app routes

@author:
@version: 2025.11
"""

from flask import Blueprint, abort, current_app, flash, redirect, render_template, request, url_for
from werkzeug.wrappers import Response

from .retrieval import get_data_from_db

main = Blueprint("main", __name__, url_prefix="/")


@main.route("/")
def world() -> str:
    query = """
    SELECT *
    FROM country;
    """
    rows = get_data_from_db(query)

    countries = [dict(row) for row in rows]

    for row in countries:
        if row["area"] and row["area"] > 0 and row["population_2023"]:
            row["density"] = round(row["population_2023"] / row["area"], 2)
        else:
            row["density"] = None

    return render_template("world.jinja", countries=countries)




@main.get("/region", defaults={"name": None})
@main.get("/region/<string:name>")
def region(name: str | None) -> str | Response:
    """Display region information"""
    if not name:
        return render_template(
            "region.jinja",
            countries=[],
            search_regions=current_app.config["regions"],
            message="Please select a continental region to view countries."
        )

    if name not in current_app.config["regions"]:
        return render_template(
            "region.jinja",
            countries=[],
            search_regions=current_app.config["regions"],
            message=f"Region '{name}' not found."
        )

    query = """
        SELECT
            c.name,
            c.official_name,
            ci.name AS capital_name,
            c.continental_region,
            c.subregion,
            c.area,
            c.population_2023,
            c.government_system
        FROM country c
        JOIN city ci ON c.capital = ci.id
        WHERE c.continental_region = ?
        ORDER BY c.name;
    """
    countries = [dict(row) for row in get_data_from_db(query, (name,))]

    for row in countries:
        if row["area"] and row["area"] > 0 and row["population_2023"]:
            row["density"] = round(row["population_2023"] / row["area"], 2)
        else:
            row["density"] = None

    return render_template(
        "region.jinja",
        countries=countries,
        search_regions=current_app.config["regions"],
        selected_region=name
    )


@main.get("/subregion", defaults={"name": None})
@main.get("/subregion/<string:name>")
def subregion(name: str | None) -> str | Response:
    """Display subregion information"""
    if not name:
        return render_template(
            "subregion.jinja",
            countries=[],
            search_subregions=current_app.config["subregions"],
            message="Please select a subregion to view countries."
        )

    if name not in current_app.config["subregions"]:
        return render_template(
            "subregion.jinja",
            countries=[],
            search_subregions=current_app.config["subregions"],
            message=f"Subregion '{name}' not found."
        )

    query = """
        SELECT
            c.name,
            c.official_name,
            ci.name AS capital_name,
            c.continental_region,
            c.subregion,
            c.area,
            c.population_2023,
            c.government_system
        FROM country c
        JOIN city ci ON c.capital = ci.id
        WHERE c.subregion = ?
        ORDER BY c.name;
    """
    countries = [dict(row) for row in get_data_from_db(query, (name,))]

    for row in countries:
        if row["area"] and row["area"] > 0 and row["population_2023"]:
            row["density"] = round(row["population_2023"] / row["area"], 2)
        else:
            row["density"] = None

    return render_template(
        "subregion.jinja",
        countries=countries,
        search_subregions=current_app.config["subregions"],
        selected_subregion=name
    )


@main.get("/country", defaults={"name": None})
@main.get("/country/<string:name>")
def country(name: str | None) -> str | Response:
    """Display country information"""
    if not name:
        return render_template(
            "country.jinja",
            cities=[],
            search_countries=current_app.config["countries"],
            message="Please select a country to view its cities."
        )

    if name not in current_app.config["countries"]:
        return render_template(
            "country.jinja",
            cities=[],
            search_countries=current_app.config["countries"],
            message=f"Country '{name}' not found."
        )

    country_query = """
        SELECT code2, capital
        FROM country
        WHERE name = ?
    """
    country_data = get_data_from_db(country_query, (name,))
    country_code = country_data[0]["code2"]
    capital_id = country_data[0]["capital"]

    cities_query = """
        SELECT id, name, admin_region, population
        FROM city
        WHERE country_code = ?
        ORDER BY population DESC
    """
    cities = [dict(row) for row in get_data_from_db(cities_query, (country_code,))]
    

    for row in cities:
        row["is_capital"] = (row["id"] == capital_id)

    return render_template(
        "country.jinja",
        cities=cities,
        search_countries=current_app.config["countries"],
        country_name=name
    )