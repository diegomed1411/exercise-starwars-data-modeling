import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User (Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    favorites_character_id = Column(Integer, ForeignKey('characterFavorites.id'))
    planetFavorites = relationship('Character_favorites')
    favorites_planets_id = Column(Integer, ForeignKey('planetFavorites.id'))
    planetFavorites = relationship('Planet_favorites')
    


class Character (Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False )
    gender = Column(String(250), nullable=False )
    height = Column(Integer, nullable=False )
    skin_color = Column(String(250), nullable=False )
    eye_color = Column(String(250), nullable=False )
    homeworld = Column(String(250), ForeignKey('planet.id'))
    planet = relationship('Planet')

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    population = Column(Integer, nullable=False )
    orbital_period = Column(Integer, nullable=False )
    rotation_period = Column(Integer, nullable=False )
    diameter = Column(Integer, nullable=False )
    character = relationship ('Character', backref='character')

class Character_favorites (Base):
    __tablename__ = 'characterFavorites'
    id = Column(Integer, primary_key=True)
    id_character = Column(Integer, ForeignKey('character.id'))
    character = relationship('Character')
    user = relationship('User')

class Planet_favorites (Base):
    __tablename__ = 'planetFavorites'
    id= Column(Integer, primary_key=True)
    id_planet = Column(Integer, ForeignKey('planet.id'))
    planet = relationship('Planet')
    user = relationship('User')
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')