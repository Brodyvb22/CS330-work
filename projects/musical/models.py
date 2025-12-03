from __init__ import db

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    sex = db.Column(db.String(10))
    year = db.Column(db.String(10))


    roles = db.relationship('Role', backref='student')
    crew_assignments = db.relationship('Crew', backref='student')

    def __repr__(self):
        return f"<Student {self.name}>"

class Production(db.Model):
    __tablename__ = 'productions'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    subtitle = db.Column(db.String(200))
    cover_image = db.Column(db.String(200))
    dates = db.Column(db.String(200))
    location = db.Column(db.String(200))
    price = db.Column(db.Float)
    copyright = db.Column(db.String(200))
    notes = db.Column(db.String(500))


    roles = db.relationship('Role', backref='production')
    crew = db.relationship('Crew', backref='production')
    creative_team = db.relationship('CreativeTeam', backref='production')
    songs = db.relationship('Song', backref='production')

    def __repr__(self):
        return f"<Production {self.title}>"

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)        
    group_name = db.Column(db.String(100))                  
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=True)
    production_id = db.Column(db.Integer, db.ForeignKey('productions.id'), nullable=True)


    def __repr__(self):
        return f"<Role {self.name}>"

class Crew(db.Model):
    __tablename__ = 'crew'
    id = db.Column(db.Integer, primary_key=True)
    job = db.Column(db.String(100))                         
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=True)
    production_id = db.Column(db.Integer, db.ForeignKey('productions.id'), nullable=True)

    def __repr__(self):
        return f"<Crew {self.job}>"

class CreativeTeam(db.Model):
    __tablename__ = 'creative_team'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)       
    role = db.Column(db.String(100), nullable=False)       
    production_id = db.Column(db.Integer, db.ForeignKey('productions.id'), nullable=True)

    def __repr__(self):
        return f"<CreativeTeam {self.name} - {self.role}>"

class Song(db.Model):
    __tablename__ = 'songs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    act = db.Column(db.String(50))
    production_id = db.Column(db.Integer, db.ForeignKey('productions.id'), nullable=True)

    performers = db.relationship('SongPerformer', backref='song')

    def __repr__(self):
        return f"<Song {self.title}>"

class SongPerformer(db.Model):
    __tablename__ = 'song_performers'
    id = db.Column(db.Integer, primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)

    role = db.relationship('Role', backref='song_performances')

    def __repr__(self):
        return f"<SongPerformer song_id={self.song_id} role_id={self.role_id}>"
