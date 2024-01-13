#!/usr/bin/python3
"""Defines classes for a singly linked list"""


class Node:
    """Defines a node of a singly linked  list"""

    def __init__(self, data, next_node=None):
        """Initilaizes the node of a singly linked list
        Args:
            data(int): value contained in a single node
            next_node(Addres): Address to to the next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets the data of a node"""
        return self.__data

    @property
    def next_node(self):
        """Gets the value of the address of the next node"""
        return self.__next_node

    @data.setter
    def data(self, value):
        """Sets the value of a node"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        """Sets the address of the next node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list"""
    def __init__(self):
        """Initializes a new singly linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """inserts a new Node into the correct sorted\
                position in the list (increasing order)
        Args:
            value(Node): The new node to insert
        """
        new = Node(value)

        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head

            while (temp.next_node is not None) and\
                    (temp.next_node.data < value):
                temp = temp.next_node
            new.next_node = temp.next_node
            temp.next_node = new

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
