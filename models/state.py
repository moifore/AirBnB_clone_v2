#!/usr/bin/python3
""" State Module for HBNB project """

import models
from os import getenv

from models.base_model import Base
from models.base_model import BaseModel
from models.city import City
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class State(BaseModel):
    """ State class that represents a state for a MySQL database 
        
        This class inherits from SQLAlchemy Base and links to MySQL

        Attributes:
        __tablename__ (str): The name of the MySQL table to store States
        name (sqlalchemy String): Name of the state
        cities (sqlalchemy relationship): State-City relationship
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")
    
    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """ Get list of City objects"""
            city_list = []
            for city in list(models.storage.all(City).values()):
                city_list.append(city)
            return city_list
