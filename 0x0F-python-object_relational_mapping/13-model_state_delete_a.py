#!/usr/bin/python3
"""Deleting records from the database the database
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Unpack command line arguments
    username, password, dbName = sys.argv[1:]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password,
                                   dbName), pool_pre_ping=True)

    # Create all tables defined in the models
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    database = Session()

    # retrieve the record from the database that matches
    # the filtering pattern
    retrievedMatches = database.query(
        State).filter(State.name.like('%a%')).all()

    # Iterate through the array of returned matches
    # then use the delete method from the database
    # Delete the record then commit changes
    for record in retrievedMatches:
        database.delete(record)

    database.commit()
