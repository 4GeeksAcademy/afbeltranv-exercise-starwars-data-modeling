import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String, nullable=False)
    email=Column(String, nullable=False)
    password=Column(String, nullable=False)

class Characters(Base):
    __tablename__ = 'Characters'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    character_name = Column(String, nullable=False)
    character_gender = Column(String, nullable=False)
    character_height = Column(String, nullable=False)
    character_mass = Column(String, nullable=False)
    character_hair_color = Column(String, nullable=False)
    character_skin_color = Column(String, nullable=False)
    character_eye_color = Column(String, nullable=False)
    character_birth_year = Column(String, nullable=False)
    character_home_world = Column(String, nullable=False)

class Planets(Base):
    __tablename__ = 'Planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planet_name = Column(String, nullable=False)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    diameter = Column(Integer, nullable=False)
    climate = Column(String, nullable=False)
    gravity = Column(Integer, nullable=False)
    terrain = Column(String, nullable=False)   

class Favorites(Base):
    __tablename__ = 'Favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)    
    Related_User = Column(Integer, ForeignKey('User.id'))
    user=relationship(User)
    Favorite_Characters = Column(Integer, ForeignKey('Characters.id'))
    character=relationship(Characters)
    Favorite_Planets = Column(Integer, ForeignKey('Planets.id'))
    planet=relationship(Planets)


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
