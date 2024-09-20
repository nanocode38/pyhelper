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
# 2602422835@qq.com
# nanocode38

"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PYHELPER--PyHelper--pyhelper
# Pyhelper - Packages that provide more helper tools for Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-----------------------------------------------------
Pyhelper is a set of packages designed to make writing Python programs better.
It is built on Python 3.11 and contains a rich set of classes and functions.
The package is highly portable and works perfectly on Windows
Python packages containing all sorts of useful data structures, functions,
classes, etc. that Python doesn't have

applied environment: Microsoft Windows 10, Python 3.8+
Copyright (C)
By nanocode38 nanocode24@outlook.com
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
New feature: gamehelpers.game_help_window

<2024.6.30> Version 1.2.0
Update: Update Class Stack and Document
New: Test

<2024.7.20> Version 2.1.0
Update: dtyping, test
Constant names with lowercase letters are not allowed
Reset the code format
Reset the document format
Delete: get_doc()

<2024.7.23> Version 2.2.0
Rename: dtyping -> type
Reset the code format
Update: README.md, pyhelper.gamehelpers.pghelper.draw_background()
New: type.DictType, type.ListType, type.TupleType, type.SetType, type.FrozenSetType, type.FrozenSet
Debug: Color.to_css/rgba(): Constant names with lowercase letters are not allowed

<2024.8.18> Version 2.3.1
Fix: pyhelper.color's names
Fix: PI and E raise ConstantError when pyhelper.mathhelper is imported multiple times
Fix: Cannot use pyhelper.type.Int, Float, String, List, Tuple, Dict, Set, FrozenSet, Bool, Boolean, Object, Bytes, Complex because it is a type annotation
Feat: pyhelper.tk
Feat: pyhelper.TKhelper
Style: Annotation used pyhelper.type

<2024.8.20> Context Manager chdir(): Temporarily change the directory

<2024.9.16> Version 2.4.0 LTS
Feat: pyhelper.color: A module about colors
Feat: chdir(), freopen()
Delete: pyhelper.type and Annotation used typing

<2024.9.20> 
Feat: pyhelper.get_command_output()
Style: Change the test style
"""
import os
import sys
from contextlib import contextmanager
from typing import *
import subprocess


__version__ = "2.4.0"
__all__ = [
            "get_version",
            'freopen',
            'chdir',
            'get_command_output',
]

if __name__ != "__main__":
    print(f"PyHelper {__version__}", end=" ")
    if os.name == "nt":
        print("(Microsoft Windows,", end=" ")
    elif os.name == "posix":
        print("(Unix,", end=" ")
    print(f"Python {sys.version_info[0]}.{sys.version_info[1]}.", end="")
    print(f"{sys.version_info[2]})")
    print("Hello from the PyHelper community!", end=" ")
    print("https://githun.com/nanocode38/pyhelper.git")

def get_version():
    """Returns the current version number of the pygwidgets package"""
    return __version__


@contextmanager
def chdir(path: str) -> None:
    """
    Context Manager: Temporarily change the current working directory to the specified path.

    :param path: The path to change the current working directory to.
    :return: The original working directory.
    """

    original_path = os.path.abspath(os.getcwd())
    os.chdir(path)
    yield
    os.chdir(original_path)


@contextmanager
def freopen(file_obj, stream=sys.stdout) -> None:
    """
    Context Manager: Temporarily change the standard output stream to the specified file.
    :param file_obj: The Object of the file to redirect the standard output stream to.
    :param stream: The stream to redirect.
    :return: The original standard output stream.
    """
    original_stream = sys.stdin
    if isinstance(stream, str):
        stream = stream.lower()
    if stream in (sys.stdin, "stdin"):
        sys.stdin = file_obj
        yield
        sys.stdin = original_stream
    elif stream in (sys.stdout, "stdout"):
        original_stream = sys.stdout
        sys.stdout = file_obj
        yield
        sys.stdout = original_stream
    elif stream in (sys.stderr, "stderr"):
        original_stream = sys.stderr
        sys.stderr = file_obj
        yield
        sys.stderr = original_stream
    else:
        raise ValueError("Invalid stream specified")





def get_command_output(command, stdout=True, stderr=False) -> Union[str, Tuple[str, str]]:
    """
    Run the command disease to get the output function
    :param command: Commands that need to be run
    :param stdout: Whether to return stdout, which defaults to True
    :param stderr: Whether to return stdout, which defaults to False
    :return str | tuple: Returns the output string/tuple after executing the command
    """
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout = result.stdout
        stderr = result.stderr
        if stdout and not stderr:
            return stdout
        elif stderr and not stdout:
            return stderr
        else:
            return stdout, stderr
    except subprocess.CalledProcessError as e:
        return e.stdout, e.stderr
