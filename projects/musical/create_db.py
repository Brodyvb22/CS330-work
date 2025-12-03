from __init__ import create_app, db

app = create_app()

with app.app_context():
    from models import Student, Production, Role, Crew, CreativeTeam, Song, SongPerformer

    db.drop_all()

    db.create_all()

    print("Database created successfully!")
