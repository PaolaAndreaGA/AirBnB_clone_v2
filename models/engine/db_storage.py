#!/usr/bin/python3
""" DB Module for HBNB project """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
import os
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


uname = os.environ.get('HBNB_MYSQL_USER')
upass = os.environ.get('HBNB_MYSQL_PWD')
host = os.environ.get('HBNB_MYSQL_HOST')
db = os.environ.get('HBNB_MYSQL_DB')
u_env = os.environ.get('HBNB_ENV')


class DBStorage:
    """DataBase Manager"""
    __engine = None
    __session = None

    def __init__(self):
        """Class constructor"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(uname, upass, host, db),
                                      pool_pre_ping=True)

        if u_env == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Return all obj of a class"""
        query_dict = {}
        classes = {
                    'State': State, 'City': City, 'User': User,
                    'Place': Place, 'Review': Review, 'Amenity': Amenity
                  }
        if cls is None:
            for key, _class in classes.items():
                result = self.__session.query(_class).all()
                for obj in result:
                    key = obj.__class__.__name__ + "." + obj.id
                    query_dict[key] = obj
        elif cls in classes.values():
            result = self.__session.query(cls).all()
            for obj in result:
                key = obj.__class__.__name__ + "." + obj.id
                query_dict[key] = obj
        return query_dict

    def new(self, obj):
        """Add new obj to a db"""
        self.__session.add(obj)

    def save(self):
        """Save the current changes in the db"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an obj"""
        if obj is not None:
            sql = self.__session.delete(obj)

    def reload(self):
        """Make tables and make a session"""
        Base.metadata.create_all(self.__engine)
        Session_m = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(Session_m)
        self.__session = Session

    def close(self):
        """call remove() method on the private session"""
        self.__session.remove()
