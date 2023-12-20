#!/usr/bin/python3
class Square:
    """A Square class"""
    def __init__(self, size=0):
        """It Initializes the square.
        
        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2
