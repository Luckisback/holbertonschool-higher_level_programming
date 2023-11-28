#!/usr/bin/python3
"""
This code lists all State objects from the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":

    u = sys.argv[1]
    p = sys.argv[2]
    bdd = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(u, pw, h, p, bdd))

    result = engine.execute(text("SELECT * FROM states;"))
    result.fetchall()

    for row in result:
        print("{}: {}".format(row[0], row[1]))
