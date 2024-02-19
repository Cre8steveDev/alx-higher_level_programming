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

    # Create a New instance of the State Class
    newState = State(name='Louisiana')

    # use the .add() method on the database session object
    # to add the new State instance/record
    database.add(newState)

    # retrieve the new instance from the database to get the id
    # which auto increments
    retrieveNewState = database.query(
        State).filter(State.name == 'Louisiana').first()

    # Print the id of the retrieved new instance
    print(retrieveNewState.id)

    # Commit changes to the database
    database.commit()
