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

<2024.10.7> Version 2.4.1
Feat: pyhelper Webside
Delete: pyhelper.get_command_output()

<2024.10.13> Version 2.4.2
Feat: pyhelper.TKhelper.FileEntry
Fix: test_all.py: File name input error
Fix: Website use Chinese Download(下载)

<2024.10.27> Version 2.4.3
FeatL pyhelper.create_shortcut
Feat: pyhelper.join_startup
Feat: pyhelper.get_startup_dir
"""
import os
import sys
from contextlib import contextmanager
from typing import *
import subprocess
import win32com.client
from pathlib import Path

__author__ = 'nanocode38'
__version__ = "2.4.3"
__all__ = [
    "get_version",
    'freopen',
    'chdir',
    'create_shortcut',
    'join_startup',
    'get_startup_dir'
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

def create_shortcut(target:Path | str, shortcut_name:str, shortcut_location:Path | str) -> None:
    """
    Creates a shortcut to the specified target file.

    :param target: Full path to the target file.
    :param shortcut_name: Name for the shortcut.
    :param shortcut_location: Location for the shortcut.
    :return: None
    """
    shell = win32com.client.Dispatch('WScript.Shell')  # Create WScript.Shell object
    shortcut = shell.CreateShortCut(os.path.join(shortcut_location, shortcut_name + '.lnk'))  # Create shortcut object
    shortcut.TargetPath = target  # Specify target path
    shortcut.WorkingDirectory = os.path.dirname(target)  # Set working directory
    shortcut.save()  # Save shortcut

def get_startup_dir() -> Path:
    """
    A function for obtaining the start-up directory
    :return: a string for the start-up directory
    """
    if platform.system() == "Windows":
        from win32com.shell import shellcon, shell
        dir_path = Path(shell.SHGetFolderPath(0, shellcon.CSIDL_STARTUP, 0, 0))
        return dir_path
    elif platform.system() == "Darwin":
        home_dir = Path(os.path.expanduser('~'))
        return home_dir / 'Library' / 'StartupItems'
    elif platform.system() == "Linux":
        # Linux 通常使用 .config/autostart 目录
        home_dir = Path(os.path.expanduser('~'))
        return home_dir / '.config' / 'autostart'
    else:
        raise OSError("Unsupported platform")

def  join_startup(target:Path | str, name:str | None = None) -> None:
    """
    A function for creating a startup shortcut in the start-up directory
    :param target: Full path to the target file.
    :param name: Name for the shortcut.
    :return: None
    """
    if not name:
        name = os.path.basename(target) + " - Shortcut"
    startup_dir = get_startup_dir()
    create_shortcut(target, name, startup_dir)

