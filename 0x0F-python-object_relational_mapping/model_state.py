#!/usr/bin/python3
"""
This defines State class that inherits from the base class
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

meta_data = MetaData()
Base = declarative_base(metadata=meta_data)


class State(Base):
    """
    Defines the class with id and name attributes of each state
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
