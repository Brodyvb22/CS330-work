from flask import Blueprint, render_template
from models import Production, Student, Role, Crew, CreativeTeam, Song, SongPerformer
from __init__ import db

view_bp = Blueprint(
    'view',
    __name__,
    template_folder='../templates/view',
    url_prefix='/view'
)

def get_production():
    return Production.query.first()


@view_bp.route('/program')
def program():
    production = get_production()

    date_list = []
    if production and production.dates:
        date_list = [d.strip() for d in production.dates.split(",")]

    return render_template(
        'program.html',
        production=production,
        dates=date_list
    )


@view_bp.route('/cast')
def cast():
    production = get_production()
    roles = production.roles if production else []
    return render_template('cast.html', roles=roles)


@view_bp.route('/crew')
def crew():
    production = get_production()
    crew_members = production.crew if production else []
    return render_template('crew.html', crew=crew_members)


@view_bp.route('/songs')
def songs():
    production = get_production()
    songs = production.songs if production else []

    for song in songs:
        song.performer_roles = [sp.role for sp in song.performers]

    return render_template('songs.html', songs=songs)


@view_bp.route('/team')
def team():
    production = get_production()
    team_members = production.creative_team if production else []
    return render_template('team.html', team=team_members)


@view_bp.route('/thanks')
def thanks():
    production = get_production()
    return render_template('thanks.html', production=production)
