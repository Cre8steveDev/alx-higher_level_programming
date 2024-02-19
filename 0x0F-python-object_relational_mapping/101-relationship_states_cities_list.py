#!/usr/bin/python3
""" prints the State object with the name passed as argument from the database
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    database = Session()

    retrieved = database.query(State).order_by(State.id)

    # iterate through
    for instance in retrieved:
        print(instance.id, instance.name, sep=": ")

        # After querying the States database, doing instance.cities
        # Will trigger another query that will get you all the
        # Cities associated with the State object
        for city_ins in instance.cities:
            print("    ", end="")
            print(city_ins.id, city_ins.name, sep=": ")
