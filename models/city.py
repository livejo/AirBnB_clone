#!/usr/bin/python3
"""
 class City that inherits from BaseModel
"""
from models.base_model import BaseModel



class City(BaseModel):
    """ defining City class """
    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        """
            Init
        """
        super().__init__(*args, **kwargs)
