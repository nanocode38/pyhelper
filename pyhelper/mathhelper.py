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
from typing import *

__all__ = [
    'calculate_pi',
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
with suppress(constant.ConstantError):
    constant.const.INF = 1e15

_PYTHON_PATH = sys.executable[:-11]
if os.name == 'nt' and _PYTHON_PATH[-6:] == 'Script':
    _PYTHON_PATH = _PYTHON_PATH[:-7]
elif os.name == 'posix' and _PYTHON_PATH[-3:] == 'bin':
    _PYTHON_PATH = _PYTHON_PATH[:-4]
_PYTHON_PATH = os.path.join(_PYTHON_PATH, 'Lib', 'site-packages', 'pyhelper')


def calculate_pi(count:int)->float:
    """
    A function that calculates PI according to a formula
    :param count: Calculate the precision of PI, the higher the value, the slower the calculation speed, the higher the precision
    :return: The result of the calculation
    """
    result =0.0
    positive = True
    for i in range(count):
        tmp =1.0 / float(i * 2 + 1)
        if positive:
            result += tmp
        else:
            result -= tmp
        positive = not positive

    return result *4.0


@functools.lru_cache
def fibonacci(number: int) -> int:
    """
    Calculate the Fibonacci sequence for the given number.
    :param number: The number in the Fibonacci sequence to be calculated.
    :return The Fibonacci sequence for the given number.
    :raise TypeError: If the input is not an int.
    :raise ValueError: If the input is a negative int.
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
    :param number: The number to be checked for primality.
    :return True if the number is prime, False otherwise.
    :raise TypeError: If the input is not an int.
    :raise ValueError: If the input is a negative int.
    """
    if not isinstance(number, int) or number <= 0:
        return False
    if number < 2:
        return False
    if number == 2:
        return True
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


# noinspection PyAugmentAssignment,PyMethodFirstArgAssignment,PyTypeChecker
class Stack(object):
    """
    Stack structure in Python PyHelper

    :param size: The maximum size of the stack. Defaults to infinity.
    :param infuse: An optional iterable to initialize the stack with. Defaults to None.
    """

    def __init__(self, infuse: Optional[Iterable] = None, size: int = math.inf):
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

    def is_lock(self) -> bool:
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
        if isinstance(other, (int, float, complex, bool, str, decimal.Decimal, Fraction)):
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
            raise TypeError("Stack can only be added with type numerical , type str , type Stack  or type iterable,"
                            + f" and cannot be added with {other.__class__.__qualname__} !")

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self = self + other
        return self

    def __mul__(self, other):
        if not isinstance(other, int):
            raise TypeError(f"Stack can only be multiplied with int, and cannot be multiplied with " +
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

    def __imul__(self, other: int):
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

    def is_full(self) -> bool:
        """
        Check if the stack is full.
        
        :return bool: True if the stack is full, False otherwise.
        """
        return len(self) == self.size

    def is_empty(self) -> bool:
        """
        Check if the stack is empty.

        return: True if the stack is empty, False otherwise.
        """
        return len(self) == 0

    def __str__(self):
        return str(self._items)

    def __repr__(self):
        return f"<class Stack({self._items!s} at 0x{id(self)})>"

    def clean(self) -> None:
        """Clear all items from the stack."""
        self._items = type(self._items)()

    def get_list(self) -> list:
        return self._items

