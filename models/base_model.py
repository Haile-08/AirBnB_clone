#!/usr/bin/python3
"""Define a class BaseModel"""
import uuid
import datetime


class BaseModel:
    """Reprsent a base model"""

    def __init__(self):
        """Class constructor"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()

    def __str__(self):
        """Print reprsentation of a class"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at"""
        self.updated_at = datetime.datetime.today()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__"""
        res = self.__dict__.copy()
        res["__class__"] = self.__class__.__name__
        res['created_at'] = self.created_at.isoformat()
        res['updated_at'] = self.updated_at.isoformat()
        return res
