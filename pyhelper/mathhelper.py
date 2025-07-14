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
# nanocode38@88.com
# nanocode38

"""
A Python module that provides mathematical-related tools, belonging to Pyhelper
Copyright (C)
"""
import functools
import math
import os
import sys
from contextlib import suppress

with suppress(ImportError):
    import numba

__all__ = [
    "calculate_pi",
    "fibonacci",
    "is_prime",
]

PI = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280
E = 2.7182818284590452353602874713526624977572470937
FAI = 0.5772156649015328606065120900824024310421593359399235988057672348848677267776646709369470632917467495

_PYTHON_PATH = sys.executable[:-11]
if os.name == "nt" and _PYTHON_PATH[-6:] == "Script":
    _PYTHON_PATH = _PYTHON_PATH[:-7]
elif os.name == "posix" and _PYTHON_PATH[-3:] == "bin":
    _PYTHON_PATH = _PYTHON_PATH[:-4]
_PYTHON_PATH = os.path.join(_PYTHON_PATH, "Lib", "site-packages", "pyhelper")


def calculate_pi(count: int) -> float:
    """
    A function that calculates PI according to a formula

    Args:
        count: Calculate the precision of PI, the higher the value, the slower the calculation speed, the higher the precision

    Returns:
        The result of the calculation

    Examples:
        >>> calculate_pi(100_000)  # doctest: +ELLIPSIS
        3.141...
    """
    result = 0.0
    positive = True
    for i in range(count):
        tmp = 1.0 / float(i * 2 + 1)
        if positive:
            result += tmp
        else:
            result -= tmp
        positive = not positive

    return result * 4.0


with suppress(NameError):
    calculate_pi = numba.jit(calculate_pi)


@functools.lru_cache
def fibonacci(number: int) -> int:
    """
    Calculate the Fibonacci sequence for the given number.

    Args:
        number: The number in the Fibonacci sequence to be calculated.

    Returns:
        The Fibonacci sequence for the given number.

    Raises:
        TypeError: If the input is not an int.
        ValueError: If the input is a negative int.

    Examples:
        >>> fibonacci(1)
        1
        >>> fibonacci(10)
        55
        >>> fibonacci(1.5)  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
            ...
        TypeError: Please pass an int argument, not a float!
        >>> fibonacci(-1)  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
            ...
        ValueError: Please pass a positive int argument!
    """

    if not isinstance(number, int):
        if number.__class__.__qualname__[0].upper() in ("A", "E", "I", "O", "U"):
            raise TypeError("Please pass an int argument, not an {0}!".format(number.__class__.__qualname__))
        raise TypeError("Please pass an int argument, not a {0}!".format(number.__class__.__qualname__))
    if number < 0:
        raise ValueError("Please pass a positive int argument!")

    if number == 0:
        return 0
    if number == 1:
        return 1
    return fibonacci(number - 1) + fibonacci(number - 2)


@functools.lru_cache
def is_prime(number: int) -> bool:
    """
    Check if the given number is a prime number.

    Args:
        number: The number to be checked for primality.

    Returns:
        True if the number is prime, False otherwise.

    Raises:
        TypeError: If the input is not an int.
        ValueError: If the input is a negative int.

    Examples:
        >>> is_prime(2)
        True
        >>> is_prime(3)
        True
        >>> is_prime(5)
        True
        >>> is_prime(7)
        True
        >>> is_prime(11)
        True
        >>> is_prime(13)
        True
        >>> is_prime(17)
        True
        >>> is_prime(19)
        True
        >>> is_prime(23)
        True
        >>> is_prime(29)
        True
        >>> is_prime(31)
        True
        >>> is_prime(37)
        True
        >>> is_prime(41)
        True
        >>> is_prime(43)
        True
        >>> is_prime(47)
        True
        >>> is_prime(53)
        True
        >>> is_prime(1)
        False
        >>> is_prime(-1)
        False
        >>> is_prime(105)
        False
        >>> is_prime(292)
        False
        >>> is_prime(63)
        False
        >>> is_prime(39)
        False
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


if __name__ == "__main__":
    import doctest

    doctest.testmod()
