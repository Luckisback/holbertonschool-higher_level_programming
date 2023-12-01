#!/usr/bin/python3

""" lists all State objects from the database hbtn_0e_6_usa"""

from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":

    us = argv[1]
    pw = argv[2]
    db = argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}\
        @localhost:3306/{}".format(us, pw, db), pool_pre_ping=True)

    """ creating session to interact with database """
    Session = sessionmaker(bind=engine)
    session = Session()
    """ retrieve the first state"""
    qy = session.query(State).filter\
        (State.name.like('%a%')).order_by(State.id)

    """ display the result """
    for state in qy:
        print("{}: {}".format(state.id, state.name))
    session.close()
