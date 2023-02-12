#!/usr/bin/python3
"""Defines a module base_model"""
import uuid
import datetime
import models


class BaseModel:
    """ A BaseModel class that defines all common
        attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """Instantation

        args: non-keyworded variable length argument.
        kwargs(key/value): key/value pair.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        now = datetime.datetime.now()
                        key = now.strftime("%A, %B %d, %Y %I:%M:%S %p")
                        setattr(self, key, value)
                    setattr(self, key, value)
        else:
            models.storage.new(self)

    def __str__(self):
        """should print: [<class name>] (<self.id>) <self.__dict__>"""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ updates the public instance attribute updated_at
            with the current datetime
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of
            __dict__ of the instance
        """
        r_dict = self.__dict__.copy()
        r_dict['__class__'] = self.__class__.__name__
        r_dict['created_at'] = self.created_at.isoformat()
        r_dict['updated_at'] = self.updated_at.isoformat()
        return r_dict
