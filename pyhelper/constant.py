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
A module that provides support for Python constants
Copyright (C)
"""
from typing import *
import unittest

__all__ = [
    'Const',
    'ConstantError',
    'Constant',
    'const'
]

class ConstantError(ArithmeticError):
    pass


class Constant(object):
    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise ConstantError('Cannot change the value of the Type Constant!')
        try:
            hash(value)
        except TypeError:
            raise ConstantError('Cannot assign a constant to a non-hashable object!')
        self.__dict__[name] = value


const = Constant()
type Const = Final


class ConstantTestCase(unittest.TestCase):
    def test_Constant(self):
        const_a = Constant()
        const_a.PI = 3.1415926
        self.assertEqual(const_a.PI, 3.1415926)
        with self.assertRaisesRegex(ConstantError, "Cannot change the value of the Type Constant!"):
            const_a.PI = 3.1415927
        self.assertEqual(const_a.PI, 3.1415926)
        with self.assertRaisesRegex(ConstantError, "Cannot assign a constant to a non-hashable object!"):
            const_a.x = [1, 2, 3]


if __name__ == "__main__":
    unittest.main()
