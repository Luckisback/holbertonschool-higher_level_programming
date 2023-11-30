#!/usr/bin/python3

""" lists all State objects from the database hbtn_0e_6_usa"""

from model_state import Base, State
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":

    us = sys.argv[1]
    pw = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(us, pw, db))

    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).order_by(State.id).first()

    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))

    """
    qry = engine.execute(text("SELECT * FROM states ORDER BY states.id LIMIT 1;"))
    result =qry.fetchall()

    for row in result:
        print("{}: {}".format(row[0], row[1]))
    """
