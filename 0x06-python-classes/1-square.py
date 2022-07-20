#!/usr/bin/python3
"""A module containing a Square class
with a private attribute

"""
class Square():
    def __init__(self, size):
        ''' Square class with a private attribute
        Args:
        size(int): Size of the square
        '''
        self.__size = size
