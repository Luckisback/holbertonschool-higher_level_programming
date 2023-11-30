#!/usr/bin/python3

""" the script that prints the State object 
    with the name passed as argument
"""

from model_state import Base, State
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":

    us = sys.argv[1]
    pas = sys.argv[2]
    da = sys.argv[3]
    nom_etat = argv[len(argv) -1]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(us, pas, da))

    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.name == nom_etat).first()

    if state is None:
        print("Not found")
    else:
        print("{}".format(state.id))
