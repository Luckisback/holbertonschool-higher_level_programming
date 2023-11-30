#!/usr/bin/python3

""" This code lists all State objects from the database hbtn_0e_6_usa """

from model_state import Base, State
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":

    u = argv[1]
    p = argv[2]
    bdd = argv[3]

    """ Connection to the database """
    engine = create_engine("mysql+mysqldb://{}:{}\
                           @localhost:3306/{}".format(u, p, bdd))

    """ Creating session to interact with the database """
    Session = sessionmaker(bind=engine)
    session = Session()

    """ Displaying all stats """
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
    session.close()
