#!/usr/bin/python3
""" City Module for HBNB project """

from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship


class City(BaseModel):
    """City class for MySQL database
    
    Attributes:
        __tablename__ (str): The name of the MySQL table to store Cities
        name (sqlalchemy String): City name
        state_id (sqlalchemy String): The state id of the city
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    
