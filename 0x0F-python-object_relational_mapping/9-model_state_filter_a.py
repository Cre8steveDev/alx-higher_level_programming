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

    Session = sessionmaker(bind=engine)
    database = Session()

    for record in database.query(State).filter(State.name.like("%a%")):
        if not record:
            print("Nothing")
        else:
            print(record.id, record.name, sep=": ")
