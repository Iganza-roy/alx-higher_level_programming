#!/usr/bin/python3
"""
a script that prints the State object with
the name passed as argument from the database hbtn_0
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_city import City

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True
            )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    joint = session.query(City, State).join(State).all()

    for city, state in joint:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
