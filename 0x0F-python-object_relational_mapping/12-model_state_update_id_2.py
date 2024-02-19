#!/usr/bin/python3
"""Inserting a New Record into the database
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
    retrievedMatch = database.query(
        State).filter(State.id == 2).first()

    # An object representing the match is returned
    # You can mutate it by reference by adjusting the
    # necessary attribute and then commit
    retrievedMatch.name = 'New Mexico'
    # Commit changes to the database
    database.commit()
