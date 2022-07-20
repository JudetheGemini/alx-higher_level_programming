#!/usr/bin/python3
"""A module containing a Square class
"""

class Square:
    """Square class with setter to private field
    """
    def __init__(self, size=0):
        """Method to initialize the square object
        Args:
            size (int): Width of the square.
        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than zero.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        
    def area(self):
        """A method that returns the area of the square.
        """
        return (self.__size ** 2)
