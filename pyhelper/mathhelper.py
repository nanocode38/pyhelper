# !/usr/bin/env python3
# -*- coding: utf-8 -*-

#   ___      _  _     _               
#  | _ \_  _| || |___| |_ __  ___ _ _ 
#  |  _/ || | __ / -_) | '_ \/ -_) '_|
#  |_|  \_, |_||_\___|_| .__/\___|_|  
#       |__/           |_|            

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
Copyright (C)
"""
import decimal
import unittest
import functools
import math
import sys
import os
from contextlib import suppress
from fractions import Fraction
from collections.abc import Iterable

import pyhelper.constant as constant
from pyhelper.type import *

__all__ = [
    'constant.const.PI',
    'constant.const.E'
    'fibonacci',
    'is_prime',
    'StackOverFlowError',
    'StackUnderFlowError',
    'StackIsCloseError',
    'Stack',
]

with suppress(constant.ConstantError):
    constant.const.PI = 3.141592653589793238462643383279
with suppress(constant.ConstantError):
    constant.const.E = 2.718281828

_PYTHON_PATH = sys.executable[:-11]
if os.name == 'nt' and _PYTHON_PATH[-6:] == 'Script':
    _PYTHON_PATH = _PYTHON_PATH[:-7]
elif os.name == 'posix' and _PYTHON_PATH[-3:] == 'bin':
    _PYTHON_PATH = _PYTHON_PATH[:-4]
_PYTHON_PATH = os.path.join(_PYTHON_PATH, 'Lib', 'site-packages', 'pyhelper')


@functools.lru_cache
def fibonacci(number: Int) -> Int:
    """
    Calculate the Fibonacci sequence for the given number.
    :param number: The number in the Fibonacci sequence to be calculated.
    :return The Fibonacci sequence for the given number.
    :raise TypeError: If the input is not an Int.
    :raise ValueError: If the input is a negative Int.
    """

    if not isinstance(number, Int):
        if number.__class__.__qualname__[0].upper() in (
                'A', 'E', 'I', 'O', 'U'):
            raise TypeError("Please pass an Int argument, not an {0}!".format(
                number.__class__.__qualname__))
        raise TypeError("Please pass an Int argument, not a {0}!".format(
            number.__class__.__qualname__))
    if number < 0:
        raise ValueError("Please pass a positive Int argument!")

    if number == 0:
        return 0
    if number == 1:
        return 1
    return fibonacci(number - 1) + fibonacci(number - 2)


def is_prime(number: Int) -> Bool:
    """
    Check if the given number is a prime number.
    :param number: The number to be checked for primality.
    :return True if the number is prime, False otherwise.
    :raise TypeError: If the input is not an Int.
    :raise ValueError: If the input is a negative Int.
    """
    if not isinstance(number, Int) or number <= 0:
        return False
    if number < 2:
        return False
    if number == 2:
        return True
    j: Int = 2
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


# noinspection PyAugmentAssignment,PyMethodFirstArgAssignment,PyTypeChecker
class Stack(Object):
    """
    Stack structure in Python PyHelper

    :param size: The maximum size of the stack. Defaults to infinity.
    :param infuse: An optional iterable to initialize the stack with. Defaults to None.
    """

    def __init__(self, infuse: Optional[Iterable] = None, size: Int = math.inf):
        self.size = size
        if infuse is None:
            self._items = []
        else:
            self._items = infuse
        self._lock = False

    def push(self, value) -> None:
        """
        Push the given value onto the stack.

        :param value: The value to be pushed onto the stack.

        :raise StackIsCloseError: If the stack is locked.
        :raise StackOverFlowError: If the stack is full.
        """
        if self._lock:
            raise StackIsCloseError
        # noinspection PyTypeChecker
        if len(self._items) >= self.size:
            raise StackOverFlowError
        self._items.append(value)

    def pop(self):
        """
        Pop the top value from the stack.

        :return The popped value.

        :raise StackIsCloseError: If the stack is locked.
        :raise StackUnderFlowError: If the stack is empty.
        """
        if self._lock:
            raise StackIsCloseError
        if len(self._items) == 0:
            raise StackUnderFlowError
        return self._items.pop()

    def __len__(self):
        return len(self._items)

    def is_lock(self) -> Bool:
        """
        Check if the stack is locked.

        :return True if the stack is locked, False otherwise.
        """
        return self._lock

    def lock(self):
        """
        Lock the stack to prevent modifications.
        """
        self._lock = True

    def unlock(self):
        """
        Unlock the stack to allow modifications.
        """
        self._lock = False

    def __add__(self, other):
        if self.is_full():
            raise StackOverFlowError
        if self.is_lock():
            raise StackIsCloseError
        if isinstance(other, (Int, Float, complex, Bool, String, decimal.Decimal, Fraction)):
            if len(self) + 1 < self.size:
                _ = Stack(self._items, self.size)
                _.push(other)
                return _
            else:
                raise StackOverFlowError

        elif isinstance(other, Stack):
            if len(self._items + other._items) <= self.size:
                _ = Stack(self._items, self.size)
                _._items += other._items
                return _
            else:
                raise StackOverFlowError

        elif isinstance(other, Iterable):
            if len(self._items + other) <= self.size:
                _ = Stack(self._items, size=self.size)
                _._items += other
                return _
            else:
                raise StackOverFlowError

        else:
            raise TypeError("Stack can only be added with type numerical , type String , type Stack  or type iterable,"
                            + f" and cannot be added with {other.__class__.__qualname__} !")

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self = self + other
        return self

    def __mul__(self, other):
        if not isinstance(other, Int):
            raise TypeError(f"Stack can only be multiplied with Int, and cannot be multiplied with " +
                            other.__class__.__qualname__ + '!')
        if len(self) * other > self.size:
            raise StackOverFlowError
        if self.is_lock():
            raise StackIsCloseError
        _ = Stack(self._items, self.size)
        _._items *= other
        return _

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other: Int):
        self = self * other
        return self

    def __getitem__(self, item):
        return self._items[item]

    def __setitem__(self, item, value):
        if self.is_lock():
            raise StackIsCloseError
        self._items[item] = value

    def __delitem__(self, item):
        if self.is_lock():
            raise StackIsCloseError
        del self._items[item]

    def __eq__(self, other):
        if not isinstance(other, Stack):
            return False
        return self._items == other._items and self.size == other.size and type(self._items) is type(other._items)

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if not isinstance(other, Stack):
            return False
        return sum(self._items) < sum(other._items)

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        if not isinstance(other, Stack):
            return False
        return sum(self._items) > sum(other._items)

    def __ge__(self, other):
        return self > other or self == other

    def is_full(self) -> Bool:
        """
        Check if the stack is full.
        
        :return Bool: True if the stack is full, False otherwise.
        """
        return len(self) == self.size

    def is_empty(self) -> Bool:
        """
        Check if the stack is empty.

        return: True if the stack is empty, False otherwise.
        """
        return len(self) == 0

    def __str__(self):
        return String(self._items)

    def __repr__(self):
        return f"<class Stack({self._items!s} at 0x{id(self)})>"

    def clean(self) -> None:
        """Clear all items from the stack."""
        self._items = type(self._items)()

    def get_list(self) -> List:
        return self._items


class Array(Object):
    def __init__(self, _items=None, *, size=105, dtype=Int, default=None):
        self.size = size
        self.type = dtype
        if _items is None:
            self._items = List(default * self.size)
        else:
            self._items = _items
            self.type = type(_items[0])
            for item in self._items:
                if not isinstance(item, self.type):
                    raise TypeError(f"All Array items must be of type {self.type.__name__}!")
            if self.type != dtype:
                raise TypeError(f"All Array dtype must be of type {self.type.__name__}!")
            self.size = len(self._items)

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        if not isinstance(value, self.type):
            raise TypeError(f"All Array items must be of type {self.type.__name__}!")
        self._items[index] = value

    def __add__(self, other):
        if not isinstance(other, Array):
            raise TypeError(f"Both operands must be of type Array!")
        return Array(self._items + other._items)

    def __sub__(self, other):
        other = Int(other)
        return Array(self._items * other)

    def count(self, x):
        return self._items.count(x)

    def index(self, x):
        return self._items.index(x)

    def __repr__(self):
        return f"<class Array({self._items!s}) at 0x{id(self)}>"

    def __eq__(self, other):
        if not isinstance(other, Array):
            return False
        return self._items == other._items

    def __ne__(self, other):
        return not self == other


# noinspection PyTypeChecker
class MathHelperTestCase(unittest.TestCase):
    def setUp(self):
        self.array1 = Array([1, 2, 3, 4, 5])
        self.array2 = Array([1, 2, 3, 4, 5])
        self.array3 = Array([6, 7, 8, 9, 10])

    def test_equality(self):
        self.assertEqual(self.array1, self.array2)
        self.assertNotEqual(self.array1, self.array3)

    def test_addition(self):
        result = self.array1 + self.array3
        expected = Array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(result, expected)

    def test_count(self):
        count = self.array1.count(3)
        self.assertEqual(count, 1)

    def test_index(self):
        index = self.array1.index(4)
        self.assertEqual(index, 3)

    def test_type_checking(self):
        with self.assertRaises(TypeError):
            Array([1, 2, 3, 4, 5], dtype=String)

        with self.assertRaises(TypeError):
            self.array1[0] = '6'

        with self.assertRaises(TypeError):
            self.array1 + [6, 7, 8, 9, 10]

    def test_fibonacci(self):
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(10), 55)
        with self.assertRaises(TypeError):
            fibonacci(1.5)
        with self.assertRaises(ValueError):
            fibonacci(-1)

    def test_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13))
        self.assertTrue(is_prime(17))
        self.assertTrue(is_prime(19))
        self.assertTrue(is_prime(23))
        self.assertTrue(is_prime(29))
        self.assertTrue(is_prime(31))
        self.assertTrue(is_prime(37))
        self.assertTrue(is_prime(41))
        self.assertTrue(is_prime(43))
        self.assertTrue(is_prime(47))
        self.assertTrue(is_prime(53))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(-1))
        self.assertTrue(is_prime(2))
        self.assertFalse(is_prime(105))
        self.assertFalse(is_prime(292))
        self.assertFalse(is_prime(63))
        self.assertFalse(is_prime(39))

    def test_Stack(self):
        import array
        from pyhelper.mathhelper import Stack, StackIsCloseError, StackOverFlowError, StackUnderFlowError
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)
        with self.assertRaises(StackUnderFlowError):
            s.pop()
        s = Stack(size=2)
        s.push(1)
        s.push(2)
        with self.assertRaises(StackOverFlowError):
            s.push(3)
        s = Stack(infuse=array.array('i'))
        s.push(1)
        s.push(2)
        with self.assertRaises(TypeError):
            s.push(1.5)
        s.lock()
        with self.assertRaises(StackIsCloseError):
            s.push(3)
        s.unlock()
        self.assertEqual(s.pop(), 2)
        # [1]
        s += array.array('i', [1, 3, 2])
        self.assertEqual(List(s.get_list()), [1, 1, 3, 2])
        self.assertFalse(s > [1, 3])
        # [1, 1, 3, 2]
        self.assertTrue(s == Stack(array.array('i', [1, 1, 3, 2])))
        self.assertFalse(s < Stack([1]))
        self.assertEqual(len(s), 4)
        self.assertEqual(s[0], s[1])
        self.assertEqual(s[3], 2)
        s[2] = 9
        self.assertEqual(s[2], 9)
        self.assertEqual(List(s.get_list()), [1, 1, 9, 2])


if __name__ == '__main__':
   unittest.main()
