from app import db

class Hasil(db.Model):
    id = db.Column(db.String(30), primary_key=True)
    species = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

db.create_all()