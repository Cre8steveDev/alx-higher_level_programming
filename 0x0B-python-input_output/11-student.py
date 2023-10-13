#!/usr/bin/python3

"""A Student class with a method that returns
    The dictionary representation of the class
 """


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Instantiation method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Method that returns dictionary rep of the class"""
        variable = self.__dict__
        serialized = {}

        if isinstance(attrs, list):
            for key, value in variable.items():
                if key in attrs:
                    serialized[key] = value
        else:
            for key, value in variable.items():
                serialized[key] = value

        return serialized

    def reload_from_json(self, json):
        """Deserialize an object from a dictionary"""
        for key, value in json.items():
            setattr(self, key, value)
