#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os

storage_type = os.environ.get('HBNB_TYPE_STORAGE')


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    if storage_type == 'db':
        state_id = Column(String(60), ForeignKey("states.id"))
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref='cities',
                              cascade="all, delete, delete-orphan")
    else:
        place_id = ''
        user_id = ''
        text = ''
