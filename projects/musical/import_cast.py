import csv
from __init__ import create_app, db
from models import Student

app = create_app()

with app.app_context():
    with open('cast.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            student = Student(
                name=row['name'],
                sex=row['sex'],
                year=row['year'] 
            )
            db.session.add(student)
        db.session.commit()
    print("All students imported successfully!")
