#!/usr/bin/python3
"""
    Object Place
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Class Place
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    lalitude = 0.0
    longitude = 0.0
    amenity_ids = []
