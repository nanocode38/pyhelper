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
This module provides utility functions for components that depend on Tkinter and belongs to Pyhelper

applied environment: Microsoft Windows 10, Python3.7+, Pygame
Copyright (C)
By nanocode38 2602422835@qq.com
2023.7.5
"""
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import threading as tr



def tkmessagebox(mode: str, title="", message=""):
    """
    This function creates a simple input box with a specified title, text, and input mode (string, integer, or float). It returns the input value as a string, integer, or float, depending on the specified mode.

    :param mode: The input mode to use. Options are 'info', 'warning', 'error', 'askyesno', 'askretrycancel', and 'askyesnocancel'.
    :param title: Optional. The title of the input box window. Default is ''.
    :param message: Optional. The text to display in the input box. Default is ''.
    :return: The input value as a string, integer, or float, depending on the specified mode.
    """
    mode = mode.lower()
    if mode == 'info':
        messagebox.showinfo(title=title, message=message)
        return None

    if mode == 'warning':
        messagebox.showwarning(title=title, message=message)
        return None

    if mode == 'error':
        messagebox.showerror(title=title, message=message)
        return None

    if mode == 'askyesno':
        return messagebox.askyesno(title=title, message=message)

    if mode == 'askretrycancel':
        return messagebox.askretrycancel(title=title, message=message)

    if mode == 'askyesnocancel':
        return messagebox.askyesnocancel(title=title, message=message)

    if mode == 'askokcancel':
        return messagebox.askokcancel(title=title, message=message)

def inputbox(text=None, mode='String',command=None, title="tk", mask=None, value=''):
    """
    This function creates a simple input box with a specified title, text, and input mode (string, integer, or float). It returns the input value as a string, integer, or float, depending on the specified mode.

    :param text: Optional. The text to display in the input box. Default is 'Input String:'.
    :param mode: Optional. The input mode to use. Options are 'String', 'Integer', or 'Float'. Default is 'String'.
    :param command: Optional. A function to call when the input is accepted. Default is None.
    :param title: Optional. The title of the input box window. Default is 'tk'.
    :param mask: Optional. A mask to apply to the input. Default is None.
    :param value: Optional. The initial value of the input box. Default is ''.
    :return: The input value as a string, integer, or float, depending on the specified mode.
    """
    def playsound():
        import winsound
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
    playsoundthread = tr.Thread(target=playsound)
    playsoundthread.start()

    mode  = mode.lower()
    if mode == 'string':
        if text is None:
            text = 'Input String:'
        if mask is None:
            a = simpledialog.askstring(title, text, initialvalue=value)
        else:
            a = simpledialog.askstring(title, text, initialvalue=value, show=mask)

    if mode in ('int', 'integer'):
        if text is None:
            text = 'Input Integer:'
        if mask is None:
            a = simpledialog.askinteger(title, text, initialvalue=value)
        else:
            a = simpledialog.askinteger(title, text, initialvalue=value, show=mask)

    if mode == 'float':
        if text is None:
            text = 'Input Float:'
        if mask is None:
            a = simpledialog.askfloat(title, text, initialvalue=value)
        else:
            a = simpledialog.askfloat(title, text, initialvalue=value, show=mask)




def pathbox(title='Python tkinter', filetypes=[]):
    """
    This function opens a file dialog using the tkinter library to allow the user to select a file.
    
    Args:
    title (str, optional): The title of the file dialog window. Defaults to 'Python tkinter'.
    filetypes (list, optional): A list of file types and extensions to display in the file dialog. Defaults to [].
    
    Returns:
    str: The path of the selected file.
    """
    from tkinter import filedialog
    tk = Tk()
    tk.withdraw()
    f_path = filedialog.askopenfilename(title=title, filetypes=filetypes)
    return f_path



def choose_colorbox(title:str='Choose Color Box'):
    """
    This function opens a new_color dialog using the tkinter library to allow the user to select a new_color.
    
    Args:
    title (str, optional): The title of the new_color dialog window. Defaults to 'Choose Color Box'.
    
    Returns:
    tuple: A tuple containing the new_color in (R, G, B) format and the new_color name in uppercase.
    """
    import tkinter.colorchooser
    r = tkinter.colorchooser.askcolor(title=title)
    r = (r[0], r[1].upper())
    return r

def get_doc():
    """Get Doc"""
    import os
    import sys
    import webbrowser
    _PYTHON_PATH = sys.executable[:-11]
    if os.name == 'nt' and _PYTHON_PATH[-6:] == 'Script':
        _PYTHON_PATH = _PYTHON_PATH[:-7]
    elif os.name == 'posix' and _PYTHON_PATH[-3:] == 'bin':
        _PYTHON_PATH = _PYTHON_PATH[:-4]
    _PYTHON_PATH = os.path.join(_PYTHON_PATH, 'Lib', 'site-packages',
                                'pyhelper')
    webbrowser.open(os.path.join(_PYTHON_PATH, 'docs', 'Pyhelper TkHelper Doc.html'))