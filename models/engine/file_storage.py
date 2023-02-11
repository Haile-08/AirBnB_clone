#!/usr/bin/python3
"""A module that store object"""
import json
from models.base_model import BaseModel


class FileStorage:
    """ serializes instances to a JSON file and deserializes
        JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        o_dict = FileStorage.__objects
        obj_dict = {}

        for obj in o_dict.keys():
            obj_dict[obj] = o_dict[obj].to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load(f)
                for obj in obj_dict.values():
                    cls = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls)(**obj))
        except FileNotFoundError:
            return
