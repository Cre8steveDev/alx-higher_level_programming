#!/usr/bin/python3

""" Write a python class that contains the class
definition of State and an instance Base = declarative_base()"""

# Import the needed Module to create the class/Schema
from sqlalchemy import Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base
from model_state import State

# # Create Metadata
# classMetaData = MetaData()
# Base = declarative_base(metadata=classMetaData)


# Class definition
class City(Base):
    """Class Definition for State"
    (Attributes):
        id: Integer
        name: String
        state_id: Integer
    """
    # define link to the mysql table name
    __tablename__ = 'cities'

    # Define the column
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
