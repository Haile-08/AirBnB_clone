#!/usr/bin/python3
"""
Define a base model class
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City

class FileStorage:
    """Serializes instances to a JSON file and deserializes
    JSON file to instances
    Arttributes:
        __file_path: string - path to the JSON file
        __objects: dictionary - empty but will store all objects
        by <class name>.id
    methods:
        all(self): returns the dictionary __objects
        new(self, obj): sets in __objects the obj with key
        save(self): serializes __objects to the JSON file
        reload(self): deserializes the JSON file to __objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        Arttributes:
            obj: all objects value  by <class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        new_dict = {}

        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(new_dict, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path, "r") as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            pass
