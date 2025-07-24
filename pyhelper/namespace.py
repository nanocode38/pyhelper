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

__all__ = ["Namespace", "NamespaceMeta"]


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
            if attr in ("using", "_using"):
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

    @classmethod
    def using(cls, target_namespace=None):
        """
        Inject members of the current namespace into the target scope

        Args：
        target_namespace: Dictionary of the target scope (typically `globals()` or `locals()`), default globals()

        Notes:
        - Magic methods and the `using` function itself will be skipped
        - Use with caution inside functions (due to local scope limitations)

        Examples:
            >>> class Math(Namespace):
            ...    PI = 3.14159
            ...    def add(a, b):
            ...       return a + b
            ...    def multiply(a, b):
            ...        return a * b
            ...
            >>> Math.using(locals())
            >>> PI
            3.14159
            >>> add(1, 2)
            3
            >>> multiply(2, 3)
            6
            >>> def egg():
            ...    Math.using(locals())
            ...    print(PI)
            ...    print(add(1, 2))
            ...
            >>> egg()
            3.14159
            3
        """
        target_namespace = globals() if target_namespace is None else target_namespace
        for name in dir(cls):
            # 跳过魔术方法
            if name.startswith("__") and name.endswith("__"):
                continue

            # 跳过using方法本身
            if name == "using":
                continue

            # 获取属性值并注入目标作用域
            value = getattr(cls, name)
            target_namespace[name] = value


if __name__ == "__main__":
    import doctest

    doctest.testmod()
