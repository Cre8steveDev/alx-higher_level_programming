#!/usr/bin/python3

""" Write a python class that contains the class
definition of State and an instance Base = declarative_base()"""

# Import the needed Module to create the class/Schema
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

# Create Metadata
classMetaData = MetaData()
Base = declarative_base(metadata=classMetaData)


# Class definition
class State(Base):
    """Class Definition for State"
    (Attributes):
        id: Integer
        name: String
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
