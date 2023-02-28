#!/usr/bin/python3
"""import"""
import json
import os.path
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
        with open(self.__file_path, "w") as file:
            file.write(json.dumps(self.__objects))
    """method read a file json"""
    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                self.__objects = json.loads(file.read())
