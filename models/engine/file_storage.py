#!/usr/bin/python3
"""import"""
import json
"""class"""


class FileStorage:
    __file_path = "file.json"
    __objects = {}
    """method Return dic"""
    def all(self):
        """"return dictionary __objects"""
        return self.__objects
    """method created key"""
    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj
    """method write in a file json"""
    def save(self):
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(new_dict, file)
    """method read a file json"""
    def reload(self):
        from models.base_model import BaseModel
        from models.amenity import Amenity
        from models.city import City
        from models.user import User
        from models.place import Place
        from models.review import Review
        from models.state import State
        try:
            with open(self.__file_path, 'r') as file:
                for value in json.loads(file.read()).values():
                    eval(value["__class__"])(**value)
        except FileNotFoundError:
            pass
