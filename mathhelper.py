# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⠻⣛⡛⢿⡛⣿⣿⠛⣿⠸⣛⡻⢿⡿⢟⣛⠿⣿⠄⣿⠻⢟⣛⢻⣿⠟⣛⡻⣿⡟⢟⣻⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⢸⣿⣷⢸⣧⡸⠏⣾⣿⢰⣿⡇⢸⡇⢨⣭⣤⣿⠄⣿⢰⣿⣿⡆⡏⢨⣭⣥⣽⡇⣾⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⢸⣭⣵⣾⣿⡇⣼⣿⣿⣼⣿⣧⣼⣷⣮⣭⣽⣿⣤⣿⢰⣯⣥⣾⣿⣦⣭⣭⣿⣧⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⣼⣿⣿⣿⣧⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿

#
# Pyhelper - Packages that provide more helper tools for Python
# Copyright (C) 2023-2024   Gao Yuhan(高宇涵)
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Library General Public
# License as published by the Free Software Foundation;
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# DON'T EVEN HAVE A PERMIT TOO!
#
# Gao Yuhan(高宇涵)
# 2602422835@qq.com
# nanocode38

"""
A Python module that provides mathematical-related tools, belonging to Pyhelper
applied environment: Microsoft Windows 10, Python3.7+
Copyright (C)
By nanocode38 2602422835@qq.com
2023.7.5
"""
import math
import sys
import os
from typing import *

__all__ = [
    'get_doc',
    'PI',
    'fibonacci',
    'is_prime',
    'StackOverFlowError',
    'StackUnderFlowError',
    'StackIsCloseError',
    'Stack',
    'BTree'
]

PI: float = 3.141592653589793

_PYTHON_PATH = sys.executable[:-11]
if os.name == 'nt' and _PYTHON_PATH[-6:] == 'Script':
    _PYTHON_PATH = _PYTHON_PATH[:-7]
elif os.name == 'posix' and _PYTHON_PATH[-3:] == 'bin':
    _PYTHON_PATH = _PYTHON_PATH[:-4]
_PYTHON_PATH = os.path.join(_PYTHON_PATH, 'Lib', 'site-packages', 'pyhelper')

def get_doc():
    import webbrowser
    webbrowser.open(os.path.join(_PYTHON_PATH, 'docs', 'Pyhelper Mathhelper Doc.html'))


class StackOverFlowError(Exception):
    pass


def fibonacci(number: int) -> int:
    """
    Calculate the Fibonacci sequence for the given number.

    number: The number in the Fibonacci sequence to be calculated.

    Returns: The Fibonacci sequence for the given number.

    Raises:
    - TypeError: If the input is not an int.
    - ValueError: If the input is a negative int.
    """

    if not isinstance(number, int):
        if number.__class__.__qualname__[0].upper() in (
        'A', 'E', 'I', 'O', 'U'):
            raise TypeError("Please pass an int argument, not an {0}!".format(
                number.__class__.__qualname__))
        raise TypeError("Please pass an int argument, not a {0}!".format(
            number.__class__.__qualname__))
    if number < 0:
        raise ValueError("Please pass a positive int argument!")

    if number == 0:
        return 0
    if number == 1:
        return 1
    return fibonacci(number - 1) + fibonacci(number - 2)


def is_prime(number: int) -> bool:
    """
    Check if the given number is a prime number.

    number: The number to be checked for primality.

    Returns: True if the number is prime, False otherwise.

    Raises:
    - TypeError: If the input is not an int.
    - ValueError: If the input is a negative int.
    """
    if type(number) != int or number <= 0:
        return False
    if number == 2: return True
    j: int = 2
    while j <= math.sqrt(number) and number % j != 0:
        j += 1
    if number % j == 0:
        return False
    return True

class StackOverFlowError(Exception):
    """Raised when the Stack is full."""
    pass

class StackUnderFlowError(Exception):
    """Raised when the Stack is empty."""
    pass

class StackIsCloseError(Exception):
    """Raised when trying to perform an action on a closed Stack."""
    pass

class Stack:
    """A stack implementation with type checking and length restriction."""

    def __init__(self, type=Any, lenght=None):
        self.__stack = []
        self.type = type
        self.len = lenght
        self.__pointer = 0
        self.__is_close = False

    @property
    def is_open(self):
        """Check if the Stack is open."""
        return not self.__is_close

    @is_open.deleter
    def is_open(self):
        del self.__is_close

    @property
    def pointer(self):
        """Get the current __pointer of the Stack."""
        return not self.__pointer

    @pointer.setter
    def pointer(self, value):
        """Set the current __pointer of the Stack."""
        if value > len(self) or value < 0:
            raise IndexError("The Stack don't have this Index!")
        self.__pointer = value

    @pointer.deleter
    def pointer(self):
        del self.__pointer

    def push(self, value):
        """Push a value to the Stack.

        Raises:
            StackOverFlowError: If the Stack is full.
            TypeError: If the value's type is not compatible with the Stack's type.
        """
        if self.__is_close:
            raise StackIsCloseError("The Stack is Close,please use open()" +
                                   "__command open the Stack")

        art1 = 'a'
        art2 = 'a'
        if len(self) == self.len and self.len != 0:
            raise StackOverFlowError("The Stack is full!")
        if not self.type == Any and type(value) != self.type:
            if self.type.__qualname__[0].upper() in ('A', 'E', 'I', 'O', 'U'):
                art1 = 'an'
            if value.__class__.__qualname__[0].upper() in ('A', 'E', 'I', 'O', 'U'):
                art2 = 'an'
            raise TypeError(
                f"The Stack's Type is {self.type.__qualname__},so" +
                f" you must set {art1} {self.type.__qualname__},not {art2}" +
                f" {value.__class__.__qualname__}!")

        if self.__pointer == len(self) - 1:
            self.__pointer += 1
        self.__stack.append(value)

    def pop(self):
        """Pop a value from the Stack.

        Raises:
            StackUnderFlowError: If the Stack is empty.
        """
        if self.__is_close:
            raise StackIsCloseError("The Stack is Close,please use open()" +
                                   "__command open the Stack")
        if len(self) == 0:
            raise StackUnderFlowError("The Stack is empty!")
        self.__pointer -= 1
        return self.__stack.pop()

    def get(self):
        """Get the value at the current __pointer of the Stack.

        Raises:
            IndexError: If the __pointer is out of range.
        """
        return self.__stack[self.__pointer]

    def peek(self):
        """Get the value at the top of the Stack.

        Raises:
            IndexError: If the Stack is empty.
        """
        return self.__stack[-1]

    def clean(self):
        """Clear the Stack."""
        if self.__is_close:
            raise StackIsCloseError("The Stack is Close,please use open()" +
                                   "__command open the Stack")
        self.__stack = []
        self.__pointer = 0

    def close(self):
        """Close the Stack."""
        self.__is_close = True

    def open(self):
        """Open the Stack"""
        self.__is_close = False

    def __len__(self):
        return len(self.__stack)


class BTree:
    def __init__(self, value, father=None):
        """
        Initialize a new BTree node with the given value and optional father.

        value: The value stored in the node.
        father: The optional parent node of the new node.
        """
        self.left = None
        self.data = value
        self.right = None
        self.father = father

    def insert_left(self, value):
        """
        Insert a new left child node with the given value.

        value: The value to be inserted in the left child node.
        """
        if self.left is not None:
            self.left.father = None
        self.left = BTree(value, self)
        return self.left

    def insert_right(self, value):
        """
        Insert a new right child node with the given value.

        value: The value to be inserted in the right child node.
        """
        if self.right is not None:
            self.right.father = None
        self.right = BTree(value, self)
        return self.right

    def delete_subtree(self, node=None):
        """
        Delete the given subtree, or the one rooted at the given node.

        node: The optional root node of the subtree to be deleted. If not provided, the root node of the tree is used.
        """
        if node is None:
            node = self

        if node.left is not None:
            node.left.father = node.father
        if node.right is not None:
            node.right.father = node.father

        if node.father is not None:
            if node == node.father.left:
                node.father.left = node.right
            else:
                node.father.right = node.right

        node.right = None
        node.left = None
        node.father = None

    def search(self, value):
        """
        Search for a node with the given value in the tree.

        value: The value to be searched for in the tree.

        Returns: The node with the given value if it is found in the tree, otherwise None.
        """
        if self.data == value:
            return self

        if self.left is not None:
            return self.left.search(value)

        if self.right is not None:
            return self.right.search(value)

        return None