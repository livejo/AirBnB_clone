#!/usr/bin/python3
"""
 class User that inherits from BaseModel
"""
from models.base_model import BaseModel



class City(BaseModel):
    """ defining User class """
    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        """
            Init
        """
        super().__init__(*args, **kwargs)
