#!/usr/bin/python3
"""
 class Review that inherits from BaseModel
"""
from models.base_model import BaseModel



class Review(BaseModel):
    """ defining User class """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
            Init
        """
        super().__init__(*args, **kwargs)
