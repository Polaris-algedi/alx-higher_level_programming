#!/usr/bin/python3

"""
Module: relationship_city

This module defines the City class representing a city.
"""
from relationship_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """
    A class representing a city.

    Attributes:
        id (int): The unique identifier for the city.
        name (str): The name of the city.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
