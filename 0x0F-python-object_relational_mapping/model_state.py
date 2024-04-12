#!/usr/bin/python3
"""
contains the class definition of a State and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class State(Base):
    """
    Inherits from Base. links to the MySQL table states
    id (Integer): column of uniquie integers
    name (String): column of a string
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
