#!/usr/bin/python3

"""
script to fetch all states from the database
"""

from sqlalchemy import (create_engine)
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
import sys
from model_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    instance = session.query(State, City).order_by(State.id).\
        filter(State.id == City.state_id).all()
    for state, city in instance:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
