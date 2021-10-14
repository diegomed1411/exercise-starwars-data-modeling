import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

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
    planet = relationship(Planet)

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
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')