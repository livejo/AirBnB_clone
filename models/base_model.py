#!/usr/bin/python3
"""
a base class for other classes to use from it
"""
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """ defining base model class """
    def __init__(self, *args, **kwargs):
        """ defines id, created_at and updated_at """
        if kwargs:
            for keys, val in kwargs.items():
                if keys != "__class__":
                    if keys == "created_at" or keys == "updated_at":
                        val = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, keys, val)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """ string representation """
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ updates attr updated_at """
        self.updated_at = datetime.now()

    def to_dict(self):
        """  returns a dictionary containing all keys/value """
        temp = self.__dict__.copy()
        temp["__class__"] = self.__class__.__name__
        temp["created_at"] = self.created_at.isoformat()
        temp["updated_at"] = self.updated_at.isoformat()
        return temp
