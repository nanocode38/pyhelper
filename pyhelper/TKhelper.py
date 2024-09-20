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
This module provides some helper functions and classes for tkinter.
Copyright (C)
"""
from tkinter import messagebox
import unittest

from typing import *
from pyhelper import tk

__all__ = ['Rect', 'get_widget_rect', 'pix_to_fontsize', 'fontsize_to_pix', 'custom_messagebox', 'show_message']

class Rect:
    """
    A Rect class for tkinter,
    :param x1, y1: the position of the rect's top left
    :param x2, y2: the position of the rect's bottom right
    Attribute(Property):
    x, y(left, top): The x, y position of top and left side
    w, h(width, height): The width/height of the rect
    right: The x position of the right side
    bottom: The y position of the bottom side
    centerx, centery : The x/y position of the rect center
    center = (centerx, centery)
    size = (w, h)
    topleft = (left, top)
    topright = (right, top)
    bottomright = (left, bottom)
    bottomleft = (left, bottom)
    midleft = (left, centery)
    midright = (right, centery)
    midtop = (centerx, top)
    midbottom = (centerx, bottom)
    """
    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        self.x, self.y = x1, y1
        self.w, self.h = x2 - x1, y2 - y1

    @property
    def width(self):
        return self.w

    @width.setter
    def width(self, value):
        self.w = value

    @property
    def height(self):
        return self.h

    @height.setter
    def height(self, value):
        self.h = value

    @property
    def size(self):
        return self.w, self.h

    @size.setter
    def size(self, value):
        self.w, self.h = value[0], value[1]

    @property
    def left(self):
        return self.x

    @left.setter
    def left(self, value):
        self.x = value

    @property
    def top(self):
        return self.y

    @top.setter
    def top(self, value):
        self.y = value

    @property
    def right(self):
        return self.x + self.w

    @right.setter
    def right(self, value):
        self.x = value - self.w

    @property
    def bottom(self):
        return self.top + self.h

    @bottom.setter
    def bottom(self, value):
        self.top = value - self.h

    @property
    def centerx(self):
        return self.left + self.w // 2

    @centerx.setter
    def centerx(self, value):
        self.left = value - self.w // 2

    @property
    def centery(self):
        return self.top + self.h // 2

    @centery.setter
    def centery(self, value):
        self.top = value - self.h // 2

    @property
    def center(self):
        return self.centerx, self.centery

    @center.setter
    def center(self, value):
        self.centerx, self.centery = value[0], value[1]

    @property
    def topleft(self):
        return self.left, self.top

    @topleft.setter
    def topleft(self, value):
        self.left, self.top = value[0], value[1]

    @property
    def topright(self):
        return self.right, self.top

    @topright.setter
    def topright(self, value):
        self.right, self.top = value[0], value[1]

    @property
    def bottomleft(self):
        return self.left, self.bottom

    @bottomleft.setter
    def bottomleft(self, value):
        self.left, self.bottom = value[0], value[1]

    @property
    def bottomright(self):
        return self.right, self.bottom

    @bottomright.setter
    def bottomright(self, value):
        self.right, self.bottom = value[0], value[1]

    @property
    def midleft(self):
        return self.left, self.centery

    @midleft.setter
    def midleft(self, value):
        self.left, self.centery = value[0], value[1]

    @property
    def midright(self):
           return self.right, self.centery

    @midright.setter
    def midright(self, value):
        self.right, self.centery = value[0], value[1]

    @property
    def midtop(self):
        return self.centerx, self.top

    @midtop.setter
    def midtop(self, value):
        self.centerx, self.top = value[0], value[1]

    @property
    def midbottom(self):
        return self.centerx, self.bottom

    @midbottom.setter
    def midbottom(self, value):
        self.centerx, self.bottom = value[0], value[1]

    def move(self, x: int, y: int) -> Self:
        """Move the rect and return the rect"""
        return Rect(x, y, x + self.w, y + self.h)

    def move_ip(self, x: int, y: int) -> None:
        """Move the rect in situ"""
        self.x, self.y = x, y

    def copy(self) -> Self:
        """Copy the self Rect"""
        return Rect(self.x, self.y, self.x + self.w, self.y + self.h)

    def pack_widget(self, widget: tk.Widget) -> None:
        """
        Put the widget in the corresponding position on the Rect
        :param widget: The tk widget to be placed
        """
        widget.place(x=self.x, y=self.y)

    def __repr__(self):
        return f"<Rect({self.x}, {self.y}, {self.x + self.w}, {self.y + self.h}) at {id(self)}>"


def get_widget_rect(widget: tk.Widget) -> Rect:
    """
    Get the corresponding Rect object through the tk widget.
    :param widget: Tk.widget object used to create Rect
    """
    x, y = widget.winfo_x(), widget.winfo_y()
    return Rect(x, y, widget.winfo_reqwidth() + x, widget.winfo_reqheight() + y)



def pix_to_fontsize(pix: int, font: tuple = ('KaiTi', 12)) -> tuple:
    root = tk.Tk()
    label = tk.Label(root, height=1, width=1, font=font)
    width, height = label.winfo_reqwidth(), label.winfo_reqheight()
    return int(pix * (1 / width)), int(pix * (1 / height))


def fontsize_to_pix(num: int, font: tuple = ('KaiTi', 12)) -> tuple:
    root = tk.Tk()
    label = tk.Label(root, height=1, width=1, font=font)
    width, height = label.winfo_reqwidth(), label.winfo_reqheight()
    return width * num, height * num


def show_message(title: str, message: str, box_type: str = 'info'):
    box_type = box_type.lower()
    if box_type == 'info':
        messagebox.showinfo(title, message)
    elif box_type == 'warning':
        messagebox.showwarning(title, message)
    elif box_type == 'error':
        messagebox.showerror(title, message)
    elif box_type == 'question':
        messagebox.askquestion(title, message)
    elif box_type == 'yesno':
        messagebox.askyesno(title, message)
    elif box_type == 'yesnocancel':
        messagebox.askyesnocancel(title, message)
    elif box_type == 'retrycancel':
        messagebox.askretrycancel(title, message)


def custom_messagebox(title: Optional[str] = None, message: Optional[str] = None, icon: Optional[str] = None,
                      _type: Optional = None, **options):
    messagebox._show(title, message, icon, _type, **options)
