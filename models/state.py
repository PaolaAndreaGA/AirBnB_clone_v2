#!/usr/bin/python3
""" State Module for HBNB project """
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    if os.environ.get('HBNB_TYPE_STORAGE') == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City",
                              backref="states",
                              cascade="all, delete, delete-orphan")

    else:
        @property
        def cities(self):
            """ Returns the list of City instances with
            state_id == current State.id """
            from models import storage
            tmp_cities = []
            all_cities = storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    tmp_cities.append(city)
            return tmp_cities
