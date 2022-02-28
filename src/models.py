import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

association_table = Table('favorites', Base.metadata,
    Column('user_id', ForeignKey('user.id')),
    Column('people_id', ForeignKey('people.id')),
    Column('planets_id', ForeignKey('planets.id')),
    Column('vehicles_id', ForeignKey('vehicles.id'))
)

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(80), nullable=False)
    password = Column(String(80), nullable=False)
    people = relationship("People", 
                            secondary=association_table)
    planets = relationship("Planets", 
                            secondary=association_table)
    vehicles = relationship("Vehicles", 
                            secondary=association_table)

class People(Base):
    __tablename__ = 'people'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    birth_year = Column(String(20))
    eye_color = Column(String(20))
    gender = Column(String(20))
    height = Column(Integer)
    homeworld = Column(String(100))
    mass = Column(Integer)
    skin_color = Column(String(20))
    # user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    climate = Column(String(20))
    diameter = Column(Integer, nullable=False)
    gravity = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    rotation_period = Column(Integer, nullable=False)
    population = Column(Integer, nullable=False)
    terrain = Column(String(20), nullable=False)
    # user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    cargo_capacity = Column(Integer)
    consumables = Column(String(50), nullable=False)
    cost_in_credits = Column(Integer, nullable=False)
    crew = Column(Integer, nullable=False)
    hyperdrive_rating = Column(String(50), nullable=False)
    manufacturer = Column(String(80), nullable=False)
    model = Column(String(80), nullable=False)
    # user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)       

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')