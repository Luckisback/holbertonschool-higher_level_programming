#!/usr/bin/python3

""" Start link class to table in database """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Cities(Base):
    """ Creation of the table States in the database hbtn_0e_6_usa """

    __tablename__='States'

    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
