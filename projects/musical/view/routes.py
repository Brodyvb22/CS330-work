from flask import Blueprint, render_template
from models import Production, Student, Role, Crew, CreativeTeam, Song, SongPerformer

view_bp = Blueprint('view', __name__, template_folder='../templates/view', url_prefix='/view')

def get_production():
    return Production.query.first()

@view_bp.route('/')
def view_index():
    p = get_production()
    return render_template('view/program.html', production=p)

@view_bp.route('/program')
def program():
    production = get_production()
    return render_template('view/program.html', production=production)

@view_bp.route('/cast')
def cast():
    production = get_production()
    roles = production.roles if production else []
    return render_template('view/cast.html', roles=roles, production=production)

@view_bp.route('/crew')
def crew():
    production = get_production()
    crew_members = production.crew if production else []
    return render_template('view/crew.html', crew=crew_members, production=production)

@view_bp.route('/team')
def team():
    production = get_production()
    team_members = production.creative_team if production else []
    return render_template('view/team.html', team=team_members, production=production)

@view_bp.route('/songs')
def songs():
    production = get_production()
    songs = production.songs if production else []

    for s in songs:
        s.performer_roles = [sp.role for sp in s.performers]

    grouped = {'1': [], '2': []}
    for s in songs:
        a = (s.act or '').strip()
        if a == '1':
            grouped['1'].append(s)
        elif a == '2':
            grouped['2'].append(s)

    return render_template('view/songs.html', grouped_songs=grouped, production=production)

@view_bp.route('/thanks')
def thanks():
    production = get_production()
    return render_template('view/thanks.html', production=production)
