#!/usr/bin/python3

"""A class definition for MyList"""


class MyList(list):

    """MyList inherits from the list class"""

    def print_sorted(self):
        """Sorts the elements in the class"""
        list_sorted = sorted(self)
        print(list_sorted)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
