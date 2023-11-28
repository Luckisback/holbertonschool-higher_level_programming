#!/usr/bin/python3

""" The script that prints the State object with the name passed as argument """

from model_state import Base, State
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":

    us = sys.argv[1]
    pas = sys.argv[2]
    dbase = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(us, pas, dbase))

    Session = sessionmaker(bind=engine)
    session = Session()
    stateUpdate = session.query(State).filter(State.id == 2).first()
    stateUpdate.name = "New Mexico"
    session.commit()
