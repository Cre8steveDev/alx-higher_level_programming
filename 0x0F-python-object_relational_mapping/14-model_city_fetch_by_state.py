#!/usr/bin/python3
"""Fetch from multiple table
"""
import sys
from model_state import Base, State
from model_city import City
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
    retrireve = (database.query(State.name, City.id, City.name)
                 .filter(State.id == City.state_id))

    for record in retrireve:
        print(record[0] + ": (" + str(record[1]) + ") " + record[2])
