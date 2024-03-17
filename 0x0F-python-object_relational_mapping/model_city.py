#!/usr/bin/python3
"""
    ORM - SQLAlchemy
    module for city
"""


from sqlalchemy import Column, Integer, String, ForiegnKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
        City class to relate with MySQL table
    """
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(String(128), ForiegnKey('states.id'), nullable=False)
