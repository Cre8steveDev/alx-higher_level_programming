#!/usr/bin/python3
"""Start link class to table in database
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

    # Define Session Class to get access to the connection
    # Bind it to the engine - the database
    Session = sessionmaker(bind=engine)

    # Instantiate the session to a variable
    database = Session()

    # Iterate through the database using the query function et al.
    # pass the defined Class, e.g. table you want to access

    for record in database.query(State).order_by(State.id).limit(1):
        if not record:
            print("Nothing")
        else:
            print(record.id, record.name, sep=": ")
