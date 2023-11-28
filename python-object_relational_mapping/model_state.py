#!/usr/bin/python3

"""Start link class to table in database 
"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import Colum, Integer, String, Auto_increment, ForeignKey
from sqlalchemy import create_engine
from sys import argv

if __name__ == "__main__":

    Base = declarative_base()
    
    u = argv[1]
    mdp = argv[2]
    h = "localhost"
    p = 3306
    bdd = argv[3]


    class Cities(Base):

        __tablename__='States'

        id = column(Integer, urimary_Key=True, unique=True, nullable=False, autoincrement=True)
        name = column(String(128), nullable=False)

        engine = create_engine("mysql+mysqldb://{}:{}@{}:{}/{}".format(u, mdp, h, p, bdd, pool_pre_ping=True)

    Base.metadata.create_all(engine)
