#!/usr/bin/python3
"""
    prints all City objects from the database hbtn_0e_14_usa
"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """ creating connection to the MySQL server """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    """ creating session to interact with database """
    Session = sessionmaker(bind=engine)
    session = Session()

    """ query """
    result_qy = session.query(City, State).filter(City.state_id == State.id)

    """ display all cities"""
    for city, state in result_qy:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
