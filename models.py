from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pet(db.Model):

    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    species = db.Column(db.String, nullable=False)
    photo_url = db.Column(db.String)
    age = db.Column(db.String(10), nullable=False)
    notes = db.Column(db.String)
    available = db.Column(db.Boolean, default=True, nullable=False)

def connect_db(app):

    db.app = app
    db.init_app(app)