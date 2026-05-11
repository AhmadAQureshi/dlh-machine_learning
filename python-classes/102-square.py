#!/usr/bin/python3
"""This module defines a Square class with comparison operators."""


class Square:
    """This class represents a square."""

    def __init__(self, size=0):
        """Initialize a new square with size.

        Args:
            size: The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value: The new size of the square.

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than zero.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def __eq__(self, other):
        """Return True if two squares have equal area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Return True if two squares have different areas."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Return True if this square area is less than other square area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Return True if this square area is less than or equal to other."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Return True if this square area is greater than other square area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Return True if this square area is greater than or equal to other."""
        return self.area() >= other.area()