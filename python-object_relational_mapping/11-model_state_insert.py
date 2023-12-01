#!/usr/bin/python3

""" The script that prints the State object
    with the name passed as argument """

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":

    us = argv[1]
    pw = argv[2]
    bdd = argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(us, pw, bdd), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    newState = State(name="Louisiana")
    session.add(newState)
    session.commit()

    print(newState.id)

    session.close()
