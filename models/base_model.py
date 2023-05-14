#!/usr/bin/python3
"""
Define a base model class
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Base model of all classes

    Arttributes:
       id(str): handles unique user identity
       created_at: assigns current datetime
       updated_at: updates current datetime

    Methods:
       __str__: prints the class name, id, and creates dictionary
       representations of the input values
       save(self): updates instance arttributes with current datetime
       to_dict(self): returns the dictionary values of the instance obj
    """

    def __init__(self, *args, **kwargs):
        """constructor of the class

        args:
            *args(args): arguments
            **kwargs(dict): attrubute values
        """
        DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ("updated_at", "created_at"):
                        value = datetime.strptime(value, DATE_FORMAT)
                        self.__dict__[key] = value
                    else:
                        self.__dict__[key] = value
                else:
                    pass
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)

    def save(self):
        """
        update the public instance attribute updated_at
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        """
        newdict = self.__dict__.copy()
        newdict["__class__"] = self.__class__.__name__
        newdict["created_at"] = self.created_at.isoformat()
        newdict["updated_at"] = self.updated_at.isoformat()
        return newdict

    def __str__(self):
        """
        Print repsentaion of the class
        """
        class_name = self.__class__.__name__
        class_id = self.id
        class_dict = self.__dict__
        return "[{}] ({}) {}".format(class_name, class_id, class_dict)
