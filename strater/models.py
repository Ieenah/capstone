
import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.sqltypes import Date

  
DB_PATH = "postgres://bfxmjyatddohlp:443f0e849b395e9f26899ab4c3dbe61e9471c949ed60fff3b84be93d887f9b4e@ec2-34-193-112-164.compute-1.amazonaws.com:5432/ddhp8jbqaar79v"

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=DB_PATH):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    #db.create_all()

    

class Movie(db.Model):  
  __tablename__ = 'movies'
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String, nullable=False)
  release_date = db.Column(Date, nullable=False)

  def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

  def insert(self):
        db.session.add(self)
        db.session.commit()

  def update(self):
        db.session.commit()

  def delete(self):
        db.session.delete(self)
        db.session.commit()

  def __repr__(self):
        return f"<Movie id: '{self.id}' \nTitle: '{self.title}' \nRelease date: '{self.release_date}'>"


  def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release': self.release_date,
        }


class Actor(db.Model):
   __tablename__ = 'actors'

   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String, nullable=False)
   age = db.Column(db.String, nullable=False)
   gender = db.Column(db.String,nullable=False)


   def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

   def insert(self):
        db.session.add(self)
        db.session.commit()

   def update(self):
        db.session.commit()

   def delete(self):
        db.session.delete(self)
        db.session.commit()

   def __repr__(self):
        return f"<Actor id: '{self.id}' \nname: '{self.name}' \nAge: '{self.age}' \nGender: '{self.gender}'>"


   def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'release': self.age,
            'gender': self.gender
        }
