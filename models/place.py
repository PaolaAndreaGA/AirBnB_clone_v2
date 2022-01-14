#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from models import amenity
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import Column, String, Integer, Float, ForeignKey,\
    Table
from sqlalchemy.orm import relationship


storage_type = os.environ.get('HBNB_TYPE_STORAGE')

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True,
                             nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True,
                             nullable=False)
                      )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    if storage_type == 'db':
        reviews = relationship("Review",
                               backref="place",
                               cascade="all, delete, delete-orphan")
        amenities = relationship("Amenity",
                                 secondary=place_amenity,
                                 viewonly=False)
    else:
        @property
        def reviews(self):
            """returns the list of Review instances with place_id
                equals to the current Place.id"""
            from models import storage
            tmp_reviews = []
            all_reviews = storage.all(Review)
            for review in all_reviews.values():
                if review.place_id == self.id:
                    tmp_reviews.append(review)
            return tmp_reviews

        @property
        def amenities(self):
            """returns the list of Amenity instances based on
                the attribute amenity_ids that contains all Amenity.id
                linked to the Place"""
            from models import storage
            amenities_ids = []
            all_amenities = storage.all(Amenity)
            for amenity in all_amenities.values():
                if amenity.place_id == self.id:
                    amenities_ids.append(amenity.id)
            return amenities_ids

        @amenities.setter
        def amenities(self, obj):
            """handles append method for adding an Amenity.id
                to the attribute amenity_ids"""
            if isinstance(obj, Amenity):
                self.amenities.append(obj.id)
