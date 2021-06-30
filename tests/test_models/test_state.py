#!/usr/bin/python3
"""
    Test Case for state Model
"""
from models import BaseModel
from models import State
import unittest
import models


class Teststate(unittest.TestCase):
    """
        unitesst for state class
    """
    def issub_class(self):
        """
            test if state class is sub class of base model
        """
