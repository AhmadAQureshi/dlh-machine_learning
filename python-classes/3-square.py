#!/usr/bin/python3
"""This module defines a Square class with area calculation."""


class Square:
    """This class represents a square."""

    def __init__(self, size=0):
        """Initialize a new square with a validated size.

        Args:
            size: The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than zero.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Return the current square area."""
        return self.__size ** 2
