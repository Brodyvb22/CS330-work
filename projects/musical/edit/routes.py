# edit/routes.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from __init__ import db
from models import Production, Student, Role, Crew, CreativeTeam, Song, SongPerformer

edit_bp = Blueprint('edit', __name__, template_folder='../templates', url_prefix='/edit')

# -------------------------------
# Production
# -------------------------------
@edit_bp.route('/production', methods=['GET', 'POST'])
def production():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        if not title:
            flash("Title is required.", "danger")
            return redirect(url_for('edit.production'))

        new_prod = Production(
            title=title,
            subtitle=request.form.get('subtitle'),
            cover_image=request.form.get('cover_image'),
            dates=request.form.get('dates'),
            location=request.form.get('location'),
            price=float(request.form.get('price')) if request.form.get('price') else None,
            copyright=request.form.get('copyright'),
            notes=request.form.get('notes')
        )
        db.session.add(new_prod)
        db.session.commit()
        flash("Production saved successfully!", "success")
        return redirect(url_for('edit.production'))

    productions = Production.query.order_by(Production.title).all()
    return render_template('edit/production.html', productions=productions)


# -------------------------------
# Cast / Roles
# -------------------------------
@edit_bp.route('/cast', methods=['GET', 'POST'])
def cast():
    students = Student.query.order_by(Student.name).all()
    productions = Production.query.order_by(Production.title).all()
    roles = Role.query.order_by(Role.id).all()

    if request.method == 'POST':
        role_name = request.form.get('name', '').strip()
        student_id = request.form.get('student_id') or None
        production_id = request.form.get('production_id') or None
        group_name = request.form.get('group_name') or None

        if not role_name:
            flash("Role (character) name is required.", "danger")
            return redirect(url_for('edit.cast'))

        new_role = Role(
            name=role_name,
            group_name=group_name if group_name else None,
            student_id=int(student_id) if student_id else None,
            production_id=int(production_id) if production_id else None
        )
        db.session.add(new_role)
        db.session.commit()
        flash("Role added successfully!", "success")
        return redirect(url_for('edit.cast'))

    return render_template('edit/cast.html', students=students, productions=productions, roles=roles)


# -------------------------------
# Crew
# -------------------------------
@edit_bp.route('/crew', methods=['GET', 'POST'])
def crew():
    students = Student.query.order_by(Student.name).all()
    productions = Production.query.order_by(Production.title).all()
    crew_members = Crew.query.order_by(Crew.id).all()

    if request.method == 'POST':
        job = request.form.get('job', '').strip()
        student_id = request.form.get('student_id') or None
        production_id = request.form.get('production_id') or None

        if not job:
            flash("Crew job/role is required.", "danger")
            return redirect(url_for('edit.crew'))

        new_crew = Crew(
            job=job,
            student_id=int(student_id) if student_id else None,
            production_id=int(production_id) if production_id else None
        )
        db.session.add(new_crew)
        db.session.commit()
        flash("Crew member added successfully!", "success")
        return redirect(url_for('edit.crew'))

    return render_template('edit/crew.html', students=students, productions=productions, crew_members=crew_members)


# -------------------------------
# Creative Team (adults)
# -------------------------------
@edit_bp.route('/team', methods=['GET', 'POST'])
def team():
    productions = Production.query.order_by(Production.title).all()
    team_members = CreativeTeam.query.order_by(CreativeTeam.id).all()

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        role = request.form.get('role', '').strip()
        production_id = request.form.get('production_id') or None

        if not name or not role:
            flash("Both name and role are required.", "danger")
            return redirect(url_for('edit.team'))

        new_member = CreativeTeam(
            name=name,
            role=role,
            production_id=int(production_id) if production_id else None
        )
        db.session.add(new_member)
        db.session.commit()
        flash("Creative team member added successfully!", "success")
        return redirect(url_for('edit.team'))

    return render_template('edit/team.html', productions=productions, team_members=team_members)


# -------------------------------
# Songs
# -------------------------------
@edit_bp.route('/songs', methods=['GET', 'POST'])
def songs():
    productions = Production.query.order_by(Production.title).all()
    songs_list = Song.query.order_by(Song.id).all()
    roles = Role.query.order_by(Role.name).all()

    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        act = request.form.get('act')
        production_id = request.form.get('production_id') or None
        performer_ids = request.form.getlist('performers')  # list of role IDs (strings)

        if not title:
            flash("Song title is required.", "danger")
            return redirect(url_for('edit.songs'))

        new_song = Song(
            title=title,
            act=act,
            production_id=int(production_id) if production_id else None
        )
        db.session.add(new_song)
        db.session.commit()

        # Add performers
        for rid in performer_ids:
            try:
                rid_i = int(rid)
            except (ValueError, TypeError):
                continue
            sp = SongPerformer(song_id=new_song.id, role_id=rid_i)
            db.session.add(sp)
        db.session.commit()

        flash("Song added successfully!", "success")
        return redirect(url_for('edit.songs'))

    return render_template('edit/songs.html', productions=productions, songs=songs_list, roles=roles)
