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
# modify it under the terms of the GNU Library Public
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
Module supporting namespace classes

applied environment: Microsoft Windows 10, Python 3.8+
Copyright (C)
By nanocode38 nanocode38@88.com
2025.03.02
"""


class NamespaceMeta(type):
    """
    A MetaClass, inherits as MetaClass to change the class into a namespace

    Examples:
        >>> class NameSpace1(metaclass=NamespaceMeta):
        ...     def add(a, b):
        ...         return a + b
        ...     var = 1
        ...
        >>> NameSpace1.add(1, 2)
        3
        >>> NameSpace1.var
        1
    """

    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        for attr in attrs:
            if not callable(attrs[attr]):
                continue
            if attrs[attr] in object.__dict__:
                continue
            attr = str(attr)
            if str(attr).startswith("__") and str(attr).endswith("__"):
                continue
            setattr(cls, attr, staticmethod(attrs[attr]))


class Namespace(metaclass=NamespaceMeta):
    """
    A class inherits from NamespaceMeta, which is used to transform an ordinary class into a namespace class.

    Examples:
        >>> class Spam(Namespace):
        ...     a = 1
        ...     b = 2
        ...     def egg(d, e):
        ...         return d + e
        ...
        >>> Spam.a
        1
        >>> Spam.b
        2
        >>> Spam.egg(1, 2)
        3
    """

    pass


def namespace(cls: type):
    """
    A class decorator is used to transform an ordinary class into a namespace class.

    Examples:
        >>> @namespace
        ... class Spam:
        ...     a = 1
        ...     b = 2
        ...     def egg(d, e):
        ...         return d + e
        ...
        >>> Spam.a
        1
        >>> Spam.b
        2
        >>> Spam.egg(1, 2)
        3
    """
    for key, value in cls.__dict__.items():
        if not callable(value):
            continue
        if value in object.__dict__:
            continue
        key = str(key)
        if str(key).startswith("__") and str(key).endswith("__"):
            continue
        setattr(cls, key, staticmethod(value))
    return cls


if __name__ == "__main__":
    import doctest

    doctest.testmod()
