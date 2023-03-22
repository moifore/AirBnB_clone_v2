#!/usr/bin/python3
"""Defines the DBStorage engine"""

from os import getenv

from models.base_model import Base
from models.base_model import BaseModel

from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review

from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


class DBStorage:
    """Represents a database storage engine.

    Attributes:
    __engine (sqlalchemy.Engine): SQLAlchemy engine.
    __session (sqlalchemy.Session): SQLAlchemy session.
    """

    __engine = None
    __session = None

    def __init__(self):
        """Initialize a new DBStorage instance."""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(getenv("HBNB_MYSQL_USER"), getenv("HBNB_MYSQL_PWD"), getenv("HBNB_MYSQL_HOST"), getenv("HBNB_MYSQL_DB")), pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query database for all object of the given class. 
        if cls is None, queries all classes.

        Return: Dictionary of quired classes
        """

        if cls is None:
            all_obj = self.__session.query(State).all()
            all_obj.extend(self.__session.query(City).all())
            all_obj.extend(self.__session.query(Place).all())
            all_obj.extend(self.__session.query(Review).all())
            all_obj.extend(self.__session.query(Amenity).all())
            all_obj.extend(self.__session.query(User).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            all_obj = self.__session.query(cls)
        return {"{}.{}".format(type(o).__name__, o.id): o for o in all_obj}

    def new(self, obj):
        """Adds object to database current session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes to the database current session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes an object from the database current session."""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """"Initializes a new session in the database."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

        def close(self):
            """Close SQLAlchemy session."""
            self.__session.close()
