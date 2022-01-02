from app import app
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy(app)
basedir = os.path.dirname(os.path.abspath(__file__))
database = "sqlite:///" + os.path.join(basedir,"db.sqlite")
app.config["SQLALCHEMY_DATABASE_URI"]=database

class film(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
    title = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=False)
    rating = db.Column(db.String, nullable=False)
    duration = db.Column(db.String, nullable=False)
    quality = db.Column(db.String, nullable=False)
    trailer = db.Column(db.String, nullable=False)
    watch = db.Column(db.String, nullable=False)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False

db.create_all()