#!/usr/bin/python3

"""Create a Geometry Class"""


class BaseGeometry():
    """A Base Geometry class"""

    def area(self):
        """Un-implemented area method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validating an integer"""
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
