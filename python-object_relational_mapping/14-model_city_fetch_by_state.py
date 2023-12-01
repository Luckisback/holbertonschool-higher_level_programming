#!/usr/bin/python3

""" Prints all City objects from
the database hbtn_0e_14_usa """

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    us = argv[1]
    paw = argv[2]
    dtb = argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(us, paw, dtb), pool_pre_ping=True)

    """ creating session to interact with database """
    Session = sessionmaker(bind=engine)
    session = Session()
    """ change name of id = 2 """
    session.query(State).filter(State.id == 2).update({"name": "New Mexico"})
    session.commit()
    session.close()
