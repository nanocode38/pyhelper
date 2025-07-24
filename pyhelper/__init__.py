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
.
-----------------------------------------------------
Pyhelper is a set of packages designed to make writing Python programs better.
It is built on Python 3.13 and contains a rich set of classes and functions.
The package is highly portable and works perfectly on Windows
Python packages containing all sorts of useful data structures, functions,
classes, etc. that Python doesn't have

Because pypi is duplicated, this library on pypi is called nanocode38-pyhelper, but please still use pyhelper
after downloading and importing.

applied environment: Microsoft Windows 11, Python 3.8+
Copyright (C)
By nanocode38 nanocode38@88.com
2025.03.02
"""
import functools
import multiprocessing
import os
import platform
import subprocess
import sys
from abc import ABC
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Callable, Generator

__author__ = "nanocode38"
__version__ = "2.7.0"
__all__ = [
    "get_version",
    "file_reopen",
    "chdir",
    "create_shortcut",
    "join_startup",
    "get_startup_dir",
    "system",
    "Singleton",
    "timer",
    "gamehelpers",
    "color",
    "mathhelper",
    "tkhelper",
    "random",
    "namespace",
]


if __name__ != "__main__":
    print(f"PyHelper {__version__}", end=" ")
    os_type = platform.system()
    if os_type == "Windows":
        print("(Microsoft Windows,", end=" ")
    elif os_type == "Darwin":  # macOS
        print("(MacOS,", end=" ")
    elif os_type == "Linux":
        print("(Linux,", end=" ")
    else:
        print("(Unknown OS,", end=" ", file=sys.stderr)
    print(f"Python {sys.version_info[0]}.{sys.version_info[1]}.", end="")
    print(f"{sys.version_info[2]})")
    print("Hello from the PyHelper community!", end=" ")
    print("https://githun.com/nanocode38/pyhelper.git")
    if os_type not in ("Windows", "Darwin", "Linux"):
        print("Warning: Unknown OS, some functions may not work properly.", file=sys.stderr)


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


# This function is outdated, please do not use new projects
def create_shortcut(target: Path | str, shortcut_name: str, shortcut_location: Path | str) -> None:
    """
    This function is outdated, please do not use new projects
    Creates a shortcut to the specified target file.

    Args:
        target: Full path to the target file.
        shortcut_name: Name for the shortcut.
        shortcut_location: Location for the shortcut.
    """
    import win32com.client

    target = os.path.abspath(target)
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


def join_startup(target: Path | str, *args, **kwargs) -> bool:
    """
    Add a file to startup on Windows, macOS, or Linux.

    Args:
        target: Absolute path to the file/script to run at startup.
        args and kwargs: Used to be compatible with old versions of name parameters

    Returns:
        True if successful, False otherwise.

    Raises:
        OSError: If the platform is not supported.

    Notes:
        - Windows: Uses registry (HKCU) for user-level startup
        - macOS: Creates Launch Agent plist in ~/Library/LaunchAgents
        - Linux: Creates systemd user service or .desktop file
    """
    # Convert to absolute path and verify existence
    target = os.path.abspath(target)
    if not os.path.exists(target):
        print(f"Error: File not found at {target}", file=sys.stderr)
        return False

    os_type = platform.system()
    try:
        if os_type == "Windows":
            return _windows_startup(target)
        elif os_type == "Darwin":  # macOS
            return _macos_startup(target)
        elif os_type == "Linux":
            return _linux_startup(target)
        else:
            raise OSError("Unsupported platform, join_startup() is only available for Windows, MacOS and Linux systems")
    except Exception as e:
        print(f"Setup failed: {str(e)}")
        return False


def _windows_startup(file_path: str) -> bool:
    """Windows implementation using registry"""
    import winreg  # Standard library for registry access

    # Determine execution command
    cmd = f'"{file_path}"'  # Default for executables/batch files
    if file_path.endswith(".py"):
        python_exe = f'"{sys.executable}"'  # Use current Python interpreter
        cmd = f'{python_exe} "{file_path}"'

    # Create registry entry
    key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
    entry_name = "Startup_" + os.path.basename(file_path).replace(" ", "_")[:30]

    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_WRITE) as key:
            winreg.SetValueEx(key, entry_name, 0, winreg.REG_SZ, cmd)
        print(f"Added to startup: HKCU\\{key_path}\\{entry_name}")
        return True
    except WindowsError as e:
        print(f"Registry error: {str(e)}")
        return False


def _macos_startup(file_path: str) -> bool:
    """macOS implementation using LaunchAgent"""
    plist_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.startup.{os.path.basename(file_path)}</string>
    <key>ProgramArguments</key>
    <array>
        <string>{sys.executable if file_path.endswith('.py') else '/bin/sh'}</string>
        <string>{file_path}</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>StandardOutPath</key>
    <string>/tmp/{os.path.basename(file_path)}.log</string>
    <key>StandardErrorPath</key>
    <string>/tmp/{os.path.basename(file_path)}_error.log</string>
</dict>
</plist>"""

    # Create LaunchAgents directory if missing
    launch_agents_dir = os.path.expanduser("~/Library/LaunchAgents")
    os.makedirs(launch_agents_dir, exist_ok=True)

    # Write plist file
    plist_name = f"com.startup.{Path(file_path).stem}.plist"
    plist_path = os.path.join(launch_agents_dir, plist_name)

    with open(plist_path, "w") as f:
        f.write(plist_content)

    # Load the agent
    subprocess.run(["launchctl", "load", plist_path], check=True)
    print(f"LaunchAgent created at {plist_path}")
    return True


def _linux_startup(file_path: str) -> bool:
    """Linux implementation using systemd user service"""
    service_content = f"""[Unit]
Description=Startup Service: {os.path.basename(file_path)}
After=network.target

[Service]
ExecStart={'/usr/bin/python3 ' if file_path.endswith('.py') else ''}{file_path}
Restart=on-failure
Environment="DISPLAY=:0"  # Required for GUI apps

[Install]
WantedBy=default.target
"""

    # Create systemd user directory
    user_service_dir = os.path.expanduser("~/.config/systemd/user")
    os.makedirs(user_service_dir, exist_ok=True)

    # Write service file
    service_name = f"startup_{Path(file_path).stem}.service"
    service_path = os.path.join(user_service_dir, service_name)

    with open(service_path, "w") as f:
        f.write(service_content)

    # Enable and start service
    subprocess.run(["systemctl", "--user", "daemon-reload"], check=True)
    subprocess.run(["systemctl", "--user", "enable", service_name], check=True)
    subprocess.run(["systemctl", "--user", "start", service_name], check=True)

    print(f"Systemd service created at {service_path}")
    return True


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


@contextmanager
def timer(callback: Callable[[float, ...], Any] | None = None, *args, **kwargs) -> Generator[float, Any, None]:
    """
    Context Manager for Calculating Program Running Time

    Args:
        callback: Callback function, called at the end of the manager, contains at least the first parameter and the parameter type is float to accept time, Default: Do Nothing
        args: Positional parameters will be passed to the callback function
        kwargs: keyword parameters will be passed to the callback function

    Returns:
        Generator[float, Any, None]: The starting execution time (UTC time)

    Examples:
        >>> import time
        >>> import math
        >>> t0 = time.time()
        >>> time.sleep(2)
        >>> t1 = time.time() - t0
        >>> t2: int
        >>> def spam(t1: float, bar, egg):
        ...     global t2
        ...     print(egg)
        ...     print(bar)
        ...     t2 = t1
        ...
        >>> with timer(spam, 1, egg="Hello"):
        ...     time.sleep(2)
        ...
        Hello
        1
        >>> math.isclose(t1, t2, rel_tol=.1)
        True
        >>> math.isclose(t2, 2., rel_tol=.1)
        True
    """
    import time

    t = time.time()
    yield t
    if callback is not None:
        callback(time.time() - t, *args, **kwargs)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
