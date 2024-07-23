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
Helps developers work with Python types and type annotations
Copyright (C)
"""
from typing import *
from collections.abc import Iterator, Iterable

type Int = int
type Boolean = bool
type Bool = Boolean
type Number = Union[int, float]
type Float = float
type String = str
type Object = object
type Bytes = bytes
type ListType = List
type DictType = Dict
type TupleType = Tuple
type SetType = Set
type FrozenSetType = FrozenSet
type List = list
type Dict = dict
type Tuple = tuple
type Set = set
type FrozenSet = FrozenSet
type Complex = complex
