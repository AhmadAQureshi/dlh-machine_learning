#!/usr/bin/python3
"""This module defines a singly linked list."""


class Node:
    """This class represents a node in a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new node.

        Args:
            data: The integer data of the node.
            next_node: The next node in the list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node.

        Args:
            value: The new data value.

        Raises:
            TypeError: If data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node.

        Args:
            value: The next node object.

        Raises:
            TypeError: If next_node is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    """This class represents a singly linked list."""

    def __init__(self):
        """Initialize an empty singly linked list."""
        self.__head = None

    def __str__(self):
        """Return the linked list as a printable string."""
        values = []
        current = self.__head

        while current is not None:
            values.append(str(current.data))
            current = current.next_node

        return "\n".join(values)

    def sorted_insert(self, value):
        """Insert a new node in sorted increasing order.

        Args:
            value: The integer value to insert.
        """
        new_node = Node(value)

        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head

        while (
            current.next_node is not None
            and current.next_node.data < value
        ):
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node
