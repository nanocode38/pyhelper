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
applied environment: Microsoft Windows 10, Python3.7+
Copyright (C)
By nanocode38 2602422835@qq.com
2023.7.5
"""
import turtle
import enum
import __hello__
import urllib
import pathlib
import os
import sys
import string
import sysconfig
import logging
import locale
import typing
import tkinter
import json
import csv
import webbrowser
import copy
import copyreg
import abc
import decimal
import time
import timeit
import datetime
import dataclasses
import pickle
import setuptools
import six
import collections
import contextlib
import contextvars


_PYTHON_PATH = sys.executable[:-11]
if os.name == 'nt' and _PYTHON_PATH[-6:] == 'Script':
    _PYTHON_PATH = _PYTHON_PATH[:-7]
elif os.name == 'posix' and _PYTHON_PATH[-3:] == 'bin':
    _PYTHON_PATH = _PYTHON_PATH[:-4]
_PYTHON_PATH = os.path.join(_PYTHON_PATH, 'Lib', 'site-packages', 'pyhelper')

the_third_party_library_is_not_installed:list = []

try:
    import pygame
except ImportError:
    the_third_party_library_is_not_installed.append['pygame']

try:
    import requests
except ImportError:
    the_third_party_library_is_not_installed.append('requests')

try:
    import pywin32
    import pywin32con
    import pywin32api
except ImportError:
    the_third_party_library_is_not_installed.append('pywin32')
try:
    import pygal
except ImportError:
    the_third_party_library_is_not_installed.append('pygal')
try:
    import pandas
except ImportError:
    the_third_party_library_is_not_installed.append('pandas')
try:
    import matplotlib
except ImportError:
    the_third_party_library_is_not_installed.append('matplotlib')
try:
    import django
except ImportError:
    the_third_party_library_is_not_installed.append('django')
try:
    import PyAutoGUI
except ImportError:
    the_third_party_library_is_not_installed.append('PyAutoGUI')

try:
    import cv2
except ImportError:
    the_third_party_library_is_not_installed.append('OpenCV')

try:
    import numpy
except ImportError:
    the_third_party_library_is_not_installed.append('NumPy')

try:
    import PIL
except ImportError:
    the_third_party_library_is_not_installed.append('PIL')

try:
    import pyttsx3
except ImportError:
    the_third_party_library_is_not_installed.append('Pyttsx')

try:
    import bokeh
except ImportError:
    the_third_party_library_is_not_installed.append('bokeh')

try:
    import playsound
except ImportError:
    the_third_party_library_is_not_installed.append('playsound')

try:
    import nltk
except ImportError:
    the_third_party_library_is_not_installed.append('NLTK')

try:
    import holoviews
except ImportError:
    the_third_party_library_is_not_installed.append('holoviews')

def get_doc():
    """Get Docs"""
    import webbrowser
    webbrowser.open(os.path.join(_PYTHON_PATH, 'docs', 'Pyhelper Heads Doc.html'))
