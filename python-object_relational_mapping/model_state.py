#!/usr/bin/python3

"""Start link class to table in database 
"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sys import argv

Base = declarative_base()

class Cities(Base):

    __tablename__='States'

    id = Column("id", Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    name = Column("name", String(128), nullable=False)
