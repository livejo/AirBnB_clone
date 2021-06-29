#!/usr/bin/python3
"""
 class State that inherits from BaseModel
"""
from models.base_model import BaseModel



class State(BaseModel):
    """ defining State class """
    name = ""

    def __init__(self, *args, **kwargs):
        """
            Init
        """
        super().__init__(*args, **kwargs)
