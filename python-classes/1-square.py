#!/usr/bin/python3
"""This module defines a Square class with a private size attribute."""


class Square:
    """This class represents a square."""

    def __init__(self, size):
        """Initialize a new square with a size.

        Args:
            size: The size of the square.
        """
        self.__size = size
