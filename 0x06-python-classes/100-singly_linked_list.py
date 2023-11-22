#!/usr/bin/python3
"""module for a singly linked list"""


class Node:
    """"defines a node"""

    def __init__(self, data, next_node=None):
        """initializes the node with instance variables"""

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """gets data attribute"""

        return (self.__data)

    @data.setter
    def data(self, value):
        """sets data attribute"""

        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """get next_node attribute
        Returns: next node
        """

        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """set value of next node"""

        if (value is not None and not isinstance(value, Node)):
            raise TypeError('next_node must be a Node object')

        self.__next_node = value


class SinglyLinkedList:
    """defines a singly linked list"""

    def __init__(self):
        """Initializes the singly linked list"""

        self.head = None

    def __str__(self):
        """make list printable"""

        printstr = ""
        current = self.head
        while current:
            printstr += str(current.data) + "\n"
            current = current.next_node
        return printstr[:-1]

    def sorted_insert(self, value):
        """insert in a sorted fashion
        Args:
            value: what the value will be on the node
        """
        new = Node(value)
        if not self.head:
            self.head = new
            return
        if value < self.head.data:
            new.next_node = self.head
            self.head = new
            return
        current = self.head
        while current.next_node and current.next_node.data < value:
            current = current.next_node
        if current.next_node:
            new.next_node = current.next_node
        current.next_node = new
