#!/usr/bin/python3

class Node:
    """Defines a node of a singly linked  list"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @property
    def next_node(self):
        return self.__next_node

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new = Node(value)

        if self.__head == None:
            new.next_node = None
            self.head = new
        
        elif self._head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head

            while (temp.next_node is not None) and (temp.next_node.data < value):
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

