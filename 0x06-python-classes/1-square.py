#!/usr/bin/python3
"""A module containing a Square class
with a private attribute

"""
class Square:
    """Square class containing private attribute.

        Attributes:
            size (int): Width of the square
    """
    def __init__(self, size):
        """__init___ method of the class

            Args:
                size(int): Size of the square
        """
        self.__size = size
