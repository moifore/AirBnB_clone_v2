#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from hashlib import md5


classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City, "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """This class serializes instances to a JSON file & deserializes back to instances
    __file_path - path to the JSON file
    __objects - Empty dictionary that stores all objects by class id
    """

    __file_path = "file.json"
    __objects = {} 

    def all(self, cls=None):
        """Returns the list of objects of one type of class"""
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects


    def new(self, obj):
        """Adds new object to storage dictionary"""
        if obj is not None:
            self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        json_objects = {}
        for key in self.__objects:
            if key == "password":
                json_objects[key].decode()
            json_objects[key] = self.__objects[key].to_dict(save_fs=1)
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ Deletes object from storage dictionary if found"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """calls reload() method for deserializing the JSON file to objects"""
        self.remove()

    def close(self):
        """calls remove() method for deserializing the JSON file to objects"""
        self.remove()

    def get(self, cls, id):
        """ Returns the object based on the class name and its ID, 
        or None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value
        return None

    def count (self, cls=None):
        """Counts the number of object in FileStorage"""
        all_classes = classes.values()
        if not cls:
            count = 0
            for a_class in all_classes:
                count += len(models.storage.all(a_class).values())
        else:
            count = len(models.storage.all(a_class).values())
        return count
