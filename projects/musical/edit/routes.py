import os
from flask import Blueprint, render_template, request, redirect, url_for, current_app
from werkzeug.utils import secure_filename

from __init__ import db
from models import Production, Student, Role, Crew, CreativeTeam, Song, SongPerformer

edit_bp = Blueprint('edit', __name__, template_folder='../templates', url_prefix='/edit')

ALLOWED_EXT = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    if not filename:
        return False
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXT

@edit_bp.route('/production', methods=['GET', 'POST'])
def production():
    productions = Production.query.order_by(Production.title).all()
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        if not title:
            return redirect(url_for('edit.production'))

        cover_file = request.files.get('cover_image')
        filename = None
        if cover_file and cover_file.filename and allowed_file(cover_file.filename):
            filename = secure_filename(cover_file.filename)
            upload_folder = current_app.config['UPLOAD_FOLDER']
            os.makedirs(upload_folder, exist_ok=True)
            path = os.path.join(upload_folder, filename)
            cover_file.save(path)

        new_prod = Production(
            title=title,
            subtitle=request.form.get('subtitle'),
            cover_image=filename,
            dates=request.form.get('dates'),
            location=request.form.get('location'),
            price=float(request.form.get('price')) if request.form.get('price') else None,
            copyright=request.form.get('copyright'),
            notes=request.form.get('notes')
        )
        db.session.add(new_prod)
        db.session.commit()
        return redirect(url_for('edit.production'))

    return render_template('edit/production.html', productions=productions)

@edit_bp.route('/production/<int:id>/edit', methods=['GET', 'POST'])
def edit_production(id):
    prod = Production.query.get_or_404(id)
    if request.method == 'POST':
        prod.title = request.form.get('title', prod.title)
        prod.subtitle = request.form.get('subtitle', prod.subtitle)
        prod.dates = request.form.get('dates', prod.dates)
        prod.location = request.form.get('location', prod.location)
        prod.price = float(request.form.get('price')) if request.form.get('price') else prod.price
        prod.copyright = request.form.get('copyright', prod.copyright)
        prod.notes = request.form.get('notes', prod.notes)

        cover_file = request.files.get('cover_image')
        if cover_file and cover_file.filename and allowed_file(cover_file.filename):
            filename = secure_filename(cover_file.filename)
            upload_folder = current_app.config['UPLOAD_FOLDER']
            os.makedirs(upload_folder, exist_ok=True)
            cover_file.save(os.path.join(upload_folder, filename))
            prod.cover_image = filename

        db.session.commit()
        return redirect(url_for('edit.production'))

    return render_template('edit/edit_production.html', production=prod)

@edit_bp.route('/production/<int:id>/delete', methods=['POST'])
def delete_production(id):
    prod = Production.query.get_or_404(id)
    db.session.delete(prod)
    db.session.commit()
    return redirect(url_for('edit.production'))


@edit_bp.route('/cast', methods=['GET', 'POST'])
def cast():
    students = Student.query.order_by(Student.name).all()
    productions = Production.query.order_by(Production.title).all()
    roles = Role.query.order_by(Role.name).all()

    if request.method == 'POST':
        role_name = request.form.get('name', '').strip()
        if not role_name:
            return redirect(url_for('edit.cast'))

        student_id = request.form.get('student_id') or None
        production_id = request.form.get('production_id') or None
        group_name = request.form.get('group_name') or None

        new_role = Role(
            name=role_name,
            group_name=group_name if group_name else None,
            student_id=int(student_id) if student_id else None,
            production_id=int(production_id) if production_id else None
        )
        db.session.add(new_role)
        db.session.commit()
        return redirect(url_for('edit.cast'))

    return render_template('edit/cast.html', students=students, productions=productions, roles=roles)

@edit_bp.route('/role/<int:id>/edit', methods=['GET', 'POST'])
def edit_role(id):
    role = Role.query.get_or_404(id)
    students = Student.query.order_by(Student.name).all()
    productions = Production.query.order_by(Production.title).all()
    if request.method == 'POST':
        role.name = request.form.get('name', role.name)
        role.group_name = request.form.get('group_name', role.group_name)
        sid = request.form.get('student_id') or None
        pid = request.form.get('production_id') or None
        role.student_id = int(sid) if sid else None
        role.production_id = int(pid) if pid else None
        db.session.commit()
        return redirect(url_for('edit.cast'))
    return render_template('edit/edit_role.html', role=role, students=students, productions=productions)

@edit_bp.route('/role/<int:id>/delete', methods=['POST'])
def delete_role(id):
    role = Role.query.get_or_404(id)
    db.session.delete(role)
    db.session.commit()
    return redirect(url_for('edit.cast'))


@edit_bp.route('/crew', methods=['GET', 'POST'])
def crew():
    students = Student.query.order_by(Student.name).all()
    productions = Production.query.order_by(Production.title).all()
    crew_members = Crew.query.order_by(Crew.id).all()

    if request.method == 'POST':
        job = request.form.get('job', '').strip()
        if not job:
            return redirect(url_for('edit.crew'))
        student_id = request.form.get('student_id') or None
        production_id = request.form.get('production_id') or None
        new_crew = Crew(
            job=job,
            student_id=int(student_id) if student_id else None,
            production_id=int(production_id) if production_id else None
        )
        db.session.add(new_crew)
        db.session.commit()
        return redirect(url_for('edit.crew'))

    return render_template('edit/crew.html', students=students, productions=productions, crew_members=crew_members)

@edit_bp.route('/crew/<int:id>/edit', methods=['GET','POST'])
def edit_crew(id):
    member = Crew.query.get_or_404(id)
    students = Student.query.order_by(Student.name).all()
    productions = Production.query.order_by(Production.title).all()
    if request.method == 'POST':
        member.job = request.form.get('job', member.job)
        sid = request.form.get('student_id') or None
        pid = request.form.get('production_id') or None
        member.student_id = int(sid) if sid else None
        member.production_id = int(pid) if pid else None
        db.session.commit()
        return redirect(url_for('edit.crew'))
    return render_template('edit/edit_crew.html', member=member, students=students, productions=productions)

@edit_bp.route('/crew/<int:id>/delete', methods=['POST'])
def delete_crew(id):
    member = Crew.query.get_or_404(id)
    db.session.delete(member)
    db.session.commit()
    return redirect(url_for('edit.crew'))


TEAM_ROLES = [
    "Director","Assistant director","Drama director","Costume director",
    "Tech director","Set designer","Lighting designer","Make-up artist","Choreographer"
]

@edit_bp.route('/team', methods=['GET', 'POST'])
def team():
    productions = Production.query.order_by(Production.title).all()
    team_members = CreativeTeam.query.order_by(CreativeTeam.id).all()
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        role = request.form.get('role', '').strip()
        production_id = request.form.get('production_id') or None
        if not name or not role:
            return redirect(url_for('edit.team'))
        new_member = CreativeTeam(
            name=name,
            role=role,
            production_id=int(production_id) if production_id else None
        )
        db.session.add(new_member)
        db.session.commit()
        return redirect(url_for('edit.team'))
    return render_template('edit/team.html', productions=productions, team_members=team_members, team_roles=TEAM_ROLES)

@edit_bp.route('/team/<int:id>/edit', methods=['GET','POST'])
def edit_team(id):
    member = CreativeTeam.query.get_or_404(id)
    productions = Production.query.order_by(Production.title).all()
    if request.method == 'POST':
        member.name = request.form.get('name', member.name)
        member.role = request.form.get('role', member.role)
        pid = request.form.get('production_id') or None
        member.production_id = int(pid) if pid else None
        db.session.commit()
        return redirect(url_for('edit.team'))
    return render_template('edit/edit_team.html', member=member, productions=productions, team_roles=TEAM_ROLES)

@edit_bp.route('/team/<int:id>/delete', methods=['POST'])
def delete_team(id):
    member = CreativeTeam.query.get_or_404(id)
    db.session.delete(member)
    db.session.commit()
    return redirect(url_for('edit.team'))


@edit_bp.route('/songs', methods=['GET', 'POST'])
def songs():
    productions = Production.query.order_by(Production.title).all()
    songs_list = Song.query.order_by(Song.id).all()
    roles = Role.query.order_by(Role.name).all()

    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        if not title:
            return redirect(url_for('edit.songs'))
        act = request.form.get('act', '').strip()
        production_id = request.form.get('production_id') or None
        performer_ids = request.form.getlist('performers')
        new_song = Song(
            title=title,
            act=act,
            production_id=int(production_id) if production_id else None
        )
        db.session.add(new_song)
        db.session.commit()

        for rid in performer_ids:
            try:
                pid = int(rid)
            except:
                continue
            sp = SongPerformer(song_id=new_song.id, role_id=pid)
            db.session.add(sp)
        db.session.commit()
        return redirect(url_for('edit.songs'))

    return render_template('edit/songs.html', productions=productions, songs=songs_list, roles=roles)

@edit_bp.route('/song/<int:id>/edit', methods=['GET','POST'])
def edit_song(id):
    song = Song.query.get_or_404(id)
    productions = Production.query.order_by(Production.title).all()
    roles = Role.query.order_by(Role.name).all()
    if request.method == 'POST':
        song.title = request.form.get('title', song.title)
        song.act = request.form.get('act', song.act)
        pid = request.form.get('production_id') or None
        song.production_id = int(pid) if pid else None

        SongPerformer.query.filter_by(song_id=song.id).delete()
        new_performers = request.form.getlist('performers')
        for rid in new_performers:
            try:
                sp = SongPerformer(song_id=song.id, role_id=int(rid))
                db.session.add(sp)
            except:
                pass
        db.session.commit()
        return redirect(url_for('edit.songs'))
    current = [sp.role_id for sp in song.performers]
    return render_template('edit/edit_song.html', song=song, productions=productions, roles=roles, current=current)

@edit_bp.route('/song/<int:id>/delete', methods=['POST'])
def delete_song(id):
    song = Song.query.get_or_404(id)
    SongPerformer.query.filter_by(song_id=song.id).delete()
    db.session.delete(song)
    db.session.commit()
    return redirect(url_for('edit.songs'))
