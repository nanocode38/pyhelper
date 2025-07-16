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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PYHELPER--PyHelper--pyhelper
# Pyhelper - Packages that provide more helper tools for Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-----------------------------------------------------
Pyhelper is a set of packages designed to make writing Python programs better.
It is built on Python 3.13 and contains a rich set of classes and functions.
The package is highly portable and works perfectly on Windows
Python packages containing all sorts of useful data structures, functions,
classes, etc. that Python doesn't have

applied environment: Microsoft Windows 10, Python 3.8+
Copyright (C)
By nanocode38 nanocode38@88.com
2025.03.02
"""
import functools
import multiprocessing
import os
import platform
import sys
from abc import ABC, abstractmethod
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Generator

__author__ = "nanocode38"
__version__ = "2.6.2"
__all__ = [
    "get_version",
    "file_reopen",
    "chdir",
    "create_shortcut",
    "join_startup",
    "get_startup_dir",
    "system",
    "Singleton",
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
def chdir(path: str) -> Generator[None, Any, None]:
    """
    Context Manager: Temporarily change the current working directory to the specified path.

    Args:
        path: The path to change the current working directory to.

    Returns:
        The original working directory.

    Examples:
        >>> import os
        >>> this_path = os.path.abspath('.')
        >>> father_path = os.path.abspath('..')
        >>> with chdir(father_path):
        ...     os.getcwd() == father_path
        ...
        True
        >>> os.getcwd() == this_path
        True
    """

    original_path = os.path.abspath(os.getcwd())
    os.chdir(path)
    yield
    os.chdir(original_path)


@contextmanager
def file_reopen(file_obj, stream=sys.stdout) -> Generator[None, Any, None]:
    """
    Context Manager: Temporarily change the standard output stream to the specified file.

    Args:
        file_obj: The Object of the file to redirect the standard output stream to.
        stream: The stream to redirect.

    Returns:
        The original standard output stream.

    Examples:
        >>> original_stdin = sys.stdin
        >>> original_stdout = sys.stdout
        >>> if not os.path.isfile("test.in"):
        ...     os.chdir("../tests")
        >>> with open("test.in", "r", encoding="utf-8") as fb:
        ...     with file_reopen(fb, "stdin"):
        ...         print(sys.stdin == fb)
        ...         file_input = input()
        True
        >>> sys.stdin == original_stdin
        True
        >>> file_input == "Hello, World!"
        True
        >>> with open("test.out", "w", encoding="utf-8") as fb:
        ...     with file_reopen(fb, "stdout"):
        ...         print("Hello, World!")
        ...         spam = (sys.stdout == fb)
        >>> sys.stdout == original_stdout
        True
        >>> spam
        True
        >>> with open("test.out", "r", encoding="utf-8") as fb:
        ...     fb.read() == "Hello, World!\\n"
        True
        >>> with open("test.out", "w", encoding="utf-8"):
        ...     pass
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


def create_shortcut(target: Path | str, shortcut_name: str, shortcut_location: Path | str) -> None:
    """
    Creates a shortcut to the specified target file.

    Args:
        target: Full path to the target file.
        shortcut_name: Name for the shortcut.
        shortcut_location: Location for the shortcut.

    Returns:
        None
    """
    import win32com.client

    shell = win32com.client.Dispatch("WScript.Shell")  # Create WScript.Shell object
    shortcut = shell.CreateShortCut(os.path.join(shortcut_location, shortcut_name + ".lnk"))  # Create shortcut object
    shortcut.TargetPath = target  # Specify target path
    shortcut.WorkingDirectory = os.path.dirname(target)  # Set working directory
    shortcut.save()  # Save shortcut


def get_startup_dir() -> Path:
    """
    A function for obtaining the start-up directory

    Returns:
        A string for the start-up directory
    """
    if platform.system() == "Windows":
        from win32com.shell import shell, shellcon

        dir_path = Path(shell.SHGetFolderPath(0, shellcon.CSIDL_STARTUP, 0, 0))
        return dir_path
    elif platform.system() == "Darwin":
        home_dir = Path(os.path.expanduser("~"))
        return home_dir / "Library" / "StartupItems"
    elif platform.system() == "Linux":
        # Linux 通常使用 .config/autostart 目录
        home_dir = Path(os.path.expanduser("~"))
        return home_dir / ".config" / "autostart"
    else:
        raise OSError("Unsupported platform")


def join_startup(target: Path | str, name: str | None = None) -> None:
    """
    A function for creating a startup shortcut in the start-up directory

    Args:
        target: Full path to the target file.
        name: Name for the shortcut.

    Returns:
        None
    """
    if not name:
        name = os.path.basename(target) + " - Shortcut"
    startup_dir = get_startup_dir()
    create_shortcut(target, name, startup_dir)


def system(command: str, nonblocking: bool = False) -> int:
    """
    A function is used to replace the os.system()

    Args:
        command: Same as os.system(), the instruction that needs to be run
        nonblocking: Whether to run in a different process (whether not to block the current process), default False

    Returns:
        exit code
    """
    if not nonblocking:
        return os.system(command)
    else:
        multiprocessing.Process(target=os.system, args=(command,)).start()
        return 0


def get_annotation():
    """
    Returns:
        A decorator to simulate annotations in Java. This decorator is temporal
    """

    def annotation(func, *args, **kwargs):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return annotation


class Singleton(ABC):
    """
    An abstract base class to allow its subclass to be instantiated only once.

    Warning:
        If the subclass overloads the __new__() method, the parent class's __new__()
        method must be called in the __new__() method of the subclass, otherwise this abstract base class is invalid

    Examples:
        >>> class FooSingleton(Singleton):
        ...     def __init__(self):
        ...         self.foo = 1
        ...
        >>> spam = FooSingleton()
        >>> egg = FooSingleton()
        Traceback (most recent call last):
        ...
        RuntimeError: The Singleton Class can only be instantiated once
    """

    _has_instantiation = False

    def __new__(cls, *args, **kwargs):
        if cls._has_instantiation:
            raise RuntimeError("The Singleton Class can only be instantiated once")
        cls._has_instantiation = True
        return super().__new__(cls)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
