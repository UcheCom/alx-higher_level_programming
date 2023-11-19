#!/usr/bin/python3
"""
Creates the State "California" with the City "San Francisco" from a DB
"""
from sqlalchemy.orm import relationship
import sys
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    nwState = State(name='California')
    nwCity = City(name='San Francisco')
    nwState.cities.append(nwCity)

    session.add(nwState)
    session.add(nwCity)
    session.commit()
