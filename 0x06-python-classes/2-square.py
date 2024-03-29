#!/usr/bin/python3
# 0-square.py by kodizia
"""Defines a square """


class Square:
    """A Square class"""

    def __init__(self, size=0):
        """Initialize the square.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
