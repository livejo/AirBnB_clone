#!/usr/bin/python3
"""
 class Amenity that inherits from BaseModel
"""
from models.base_model import BaseModel



class Amenity(BaseModel):
    """ defining User class """
    name = ""

    def __init__(self, *args, **kwargs):
        """
            Init
        """
        super().__init__(*args, **kwargs)
