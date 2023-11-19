#!/usr/bin/python3
"""
This defines State class that inherits from the base class-
 declarative_base()
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

meta_data = MetaData()
Base = declarative_base(metadata=meta_data)


class State(Base):
    """
    Defines the class with id, name and cities attributes of each state
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('city', backref="state")
