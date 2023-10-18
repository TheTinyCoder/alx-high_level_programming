#!/usr/bin/python3
"""
Defines a singly linked list
"""


class Node:
    """
    Node class: node of a singly linked list

    Attributes:
        data (int): data of node
        next_node (Node): object of type Node
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter for data of node

        Returns: data of node
        """
        return (self.__data)

    @data.setter
    def data(self, data):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data

    @property
    def next_node(self):
        """
        Getter for next_node

        Returns: next node
        """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, next_node):
        if not isinstance(next_node, Node) and next_node is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node


class SinglyLinkedList:
    """
    SinglyLinkedList class: creates  a singly linked list
    """
    def __init__(self):
        self.__head = None

    def sorted_insert(self, data):
        """
        Inserts a new Node at the begining of the singly linked list

        Args:
            data: data of new node
        """
        new_node = Node(data, self.__head)
        self.__head = new_node

    def __str__(self):
        """
        Defines how values of a singly linked list will be printed
        """
        data = []
        node = self.__head
        while node is not None:
            data.append(node.data)
            node = node.next_node
        data_string = ""
        for i in sorted(data):
            data_string += str(i) + "\n"
        return (data_string[:-1])
