#!/usr/bin/python3
"""Define classes for a singly-linked list."""


class Node:
    """Represent a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new Node.

        Ags:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    @ property
    def data(self):
        """Get/set the data of the Node."""
        return (self.__data)

    @ data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @ property
    def next_node(self):
        """Get/set the next_node of the Node."""
        return (self.__next_node)

    @ next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represent a singly-linked list."""

    def __init__(self):
        """Initalize a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.

        The node is inserted into the list at the correct
        ordered numerical position.

        Ags:
            value (Node): The new Node to insert.
        """
        nw = Node(value)
        if self.__head is None:
            nw.next_node = None
            self.__head = nw
        elif self.__head.data > value:
            nw.next_node = self.__head
            self.__head = nw
        else:
            temp = self.__head
            while (temp.next_node is not None and
                    temp.next_node.data < value):
                temp = temp.next_node
            nw.next_node = temp.next_node
            temp.next_node = nw

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        temp = self.__head
        while temp is not None:
            values.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(values))
