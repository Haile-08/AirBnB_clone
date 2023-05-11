#!/usr/bin/python3
"""Define a base model class"""
import uuid
from datetime import datetime


class BaseModel:
	"""Base model of all classes"""
	
	DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"
	def __init__(self):
	   """constructor of the class"""
	   self.id = str(uuid.uuid4());
	   self.created_at = datetime.now();
	   self.updated_at = datetime.now();

	def save(self):
	   """update the public instance attribute updated_at"""
	   self.updated_at = datetime.now();

	def to_dict(self):
	   """returns a dictionary containing all keys/values of __dict__"""
	   self.__dict__["__class__"] = self.__class__.__name__;
	   self.__dict__["created_at"] = self.created_at.isoformat();
	   self.__dict__["updated_at"] = self.updated_at.isoformat();
	   return self.__dict__;

	def __str__(self):
	   """Print repsentaion of the class"""
	   class_name = self.__class__.__name__;
	   class_id = self.id;
	   class_dict = self.__dict__;
	   return "[{}] ({}) {}".format(class_name, class_id, class_dict);
