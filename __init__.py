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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PYHELPER--PyHelper--pyhelper
# Pyhelper - Packages that provide more helper tools for Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-----------------------------------------------------
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿|
⣿⣿⣿⣿⣿⣿⣿⠻⣛⡛⢿⡛⣿⣿⠛⣿⠸⣛⡻⢿⡿⢟⣛⠿⣿⠄⣿⠻⢟⣛⢻⣿⠟⣛⡻⣿⡟⢟⣻⣿⣿|
⣿⣿⣿⣿⣿⣿⣿⢸⣿⣷⢸⣧⡸⠏⣾⣿⢰⣿⡇⢸⡇⢨⣭⣤⣿⠄⣿⢰⣿⣿⡆⡏⢨⣭⣥⣽⡇⣾⣿⣿⣿|
⣿⣿⣿⣿⣿⣿⣿⢸⣭⣵⣾⣿⡇⣼⣿⣿⣼⣿⣧⣼⣷⣮⣭⣽⣿⣤⣿⢰⣯⣥⣾⣿⣦⣭⣭⣿⣧⣿⣿⣿⣿|
⣿⣿⣿⣿⣿⣿⣿⣼⣿⣿⣿⣧⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿|
-----------------------------------------------------
Pyhelper is a set of packages designed to make writing Python programs better.
It is built on Python 3.11 and contains a rich set of classes and functions.
The package is highly portable and works perfectly on Windows
Python packages containing all sorts of useful data structures, functions,
classes, etc. that Python doesn't have

applied environment: Microsoft Windows 10, Python3.7+
Copyright (C)
By nanocode38 2602422835@qq.com
2023.7.5
-----------------------------------------------------------------------
History:
<2023.05.16>  Version 0.1.0
Initial version, not released

<2023.08.01> Version 1.0.0
Have full documentation, the first version of a complete development system

<2023.08.03> Version 1.0.1
Update: Update Document
Fixed: Button causes event at press instant
New feature: gamehelper.game_help_window
"""
import os
import sys

import pyhelper.heads as heads
from pyhelper.main import *
import pyhelper.pgwidgets as pgwidgets
import pyhelper.pghelper as pghelper
import pyhelper.mathhelper as mathhelper
import pyhelper.true_random as true_random
import pyhelper.gamehelper as gamehelper

# version is there
__version__ = '1.0.1'
__all__ = [
    'get_version',
    'RGBColor',
    'CSSColor',
    'get_doc'
]

_PYTHON_PATH = sys.executable[:-11]
if os.name == 'nt' and _PYTHON_PATH[-6:] == 'Script':
    _PYTHON_PATH = _PYTHON_PATH[:-7]
elif os.name == 'posix' and _PYTHON_PATH[-3:] == 'bin':
    _PYTHON_PATH = _PYTHON_PATH[:-4]
_PYTHON_PATH = os.path.join(_PYTHON_PATH, 'Lib', 'site-packages', 'pyhelper')

if __name__ != '__main__':

    print(f'PyHelper {__version__} ', end='')
    if os.name == 'nt':
        print(f'(Microsoft Windows,', end=' ')
    elif os.name == 'posix':
        print(f'(Unix,', end=' ')
    print(f'Python {sys.version_info[0]}.{sys.version_info[1]}.',end='')
    print(f'{sys.version_info[2]})')
    print(f'Hello, {os.getlogin()}!')
    print('Welcome to the PyHelper community!', end=' ')
    print('https://githun.com/nanocode38/pyhelper')



def get_version():
    """Returns the current version number of the pygwidgets package"""
    return __version__

def get_doc():
    """Get Doc"""
    import webbrowser
    webbrowser.open(os.path.join(_PYTHON_PATH, 'docs', 'Pyhelper Doc.html'))