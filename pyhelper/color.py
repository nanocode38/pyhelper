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
# anocode38@88.com
# nanocode38

"""
A Python module about the Color. Contains RGBColor, HEXColor and HSLColor.
Copyright (C)
You can use this module as follows:
>>> HEXColor.RED
'#FF0000'
>>> HEXColor.YELLOW
'#FFFF00'
>>> HEXColor.to_rgb(HEXColor.RED)
(255, 0, 0)
>>> HEXColor.to_hsl(HEXColor.RED)
(0.0, 1.0, 0.5)
>>> HSLColor.RED
(0.0, 1.0, 0.5)
>>> HSLColor.YELLOW
(60.0, 1.0, 0.5)
>>> HSLColor.to_rgb(HSLColor.RED)
(255, 0, 0)
>>> HSLColor.to_hex(HSLColor.RED)
'#FF0000'
"""
import doctest
import json
import os.path

from . import Singleton

__all__ = [
    "RGBColor",
    "HSLColor",
    "HEXColor",
]


class _RGBColor(Singleton):

    def __init__(self):
        if not os.path.exists("color.json"):
            file = "pyhelper/color.json"
        else:
            file = "color.json"
        with open(file, "r") as fp:
            colors: dict = json.load(fp)
            for name, color in colors.items():
                setattr(self, str(name), tuple(color))

    def to_hex(self, r, g=None, b=None) -> str:
        """
        Convert RGBA color tuple to HEX color string.

        Args:
            r: RGBA Color.
            g: Optional. Third color component.
            b: Optional. Fourth color component.

        Returns:
            HEX color string.

        Examples:
            >>> rgb = (255, 0, 0)
            >>> RGBColor.to_hex(rgb)
            '#FF0000'
        """
        if g is None:
            g = r[1]
            b = r[2]
            r = r[0]
        r, g, b = int(r), int(g), int(b)
        return "#{:02X}{:02X}{:02X}".format(r, g, b).upper()

    def to_hsl(self, r, g=None, b=None) -> tuple:
        """
        Convert RGBA color tuple to HSL color tuple.

        Args:
            r: RGBA Color.
            g: Optional. Third color component.
            b: Optional. Fourth color component.

        Returns:
            HSL color tuple.

        Examples:
            >>> rgb = (255, 0, 0)
            >>> RGBColor.to_hsl(rgb)  # doctest: +ELLIPSIS
            (0.0, 1.0, 0.5)
        """
        if g is None:
            g = r[1]
            b = r[2]
            r = r[0]
        # Convert RGBA values from 0-255 to 0-1
        r, g, b = r / 255.0, g / 255.0, b / 255.0

        # Calculate the maximum and minimum values
        max_c = max(r, g, b)
        min_c = min(r, g, b)
        delta = max_c - min_c

        # Calculate lightness L
        l = (max_c + min_c) / 2

        # If the maximum and minimum values are the same, it's a shade of gray, so H and S are 0
        if delta == 0:
            h = 0
            s = 0
        else:
            # Calculate saturation S
            if l < 0.5:
                s = delta / (max_c + min_c)
            else:
                s = delta / (2 - max_c - min_c)

            # Calculate hue H
            if r == max_c:
                h = (g - b) / delta
            elif g == max_c:
                h = 2 + (b - r) / delta
            else:
                h = 4 + (r - g) / delta

            h = h * 60
            if h < 0:
                h += 360

        # Return HSL values
        return h, s, l


RGBColor = _RGBColor()


class _HEXColor(Singleton):

    def __init__(self):
        for key, value in RGBColor.__dict__.items():
            if isinstance(value, tuple):
                setattr(self, key, RGBColor.to_hex(value))

    @staticmethod
    def to_rgb(color: str) -> tuple:
        """
        Convert a HEX color string to RGB tuple.

        Args:
            color: HEX color string.

        Returns:
            RGB tuple.

        Examples:
            >>> HEXColor.to_rgb('#FF0000')
            (255, 0, 0)
        """
        if color.startswith("#"):
            hex_color = color[1:]
        elif color.startswith("0x"):
            hex_color = color[2:]
        else:
            hex_color = color[::]
        if len(color) == 3:
            hex_color = f"{color[0]}{color[0]}{color[1]}{color[1]} {color[2]}{color[2]}"
        r = int(hex_color[:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        return r, g, b

    @staticmethod
    def to_hsl(color: str):
        """
        Convert HEX color string to HSL color.

        Args:
            color: HEX color string

        Returns:
            HSL color tuple.

        Examples:
            >>> HEXColor.to_hsl('#FF0000')  # doctest: +ELLIPSIS
            (0.0, 1.0, 0.5)
        """
        if color.startswith("#"):
            color = color[1:]
        elif color.startswith("0x"):
            color = color[2:]
        else:
            color = color[::]
        if len(color) == 3:
            color = f"{color[0]}{color[0]}{color[1]}{color[1]} {color[2]}{color[2]}"
        return RGBColor.to_hsl(HEXColor.to_rgb(color))


HEXColor = _HEXColor()


class _HSLColor(Singleton):
    def __init__(self):
        for key, value in RGBColor.__dict__.items():
            if isinstance(value, tuple):
                setattr(self, key, RGBColor.to_hsl(value))

    def to_rgb(self, h, s=None, l=None):
        """
        Convert HSL color to RGB color.

        Args:
            h: Hue value in the range of 0 to 360.
            s: Saturation value in the range of 0.0 to 1.0. Optional.
            l: Lightness value in the range of 0.0 to 1.0. Optional.

        Returns:
            A tuple of RGB values in the range of 0 to 255.

        Examples:
            >>> HSLColor.to_rgb(0.0, 1.0, 0.5)
            (255, 0, 0)
        """
        if s is None:
            s, l = h[1], h[2]
            h = h[0]
        elif h is None:
            raise ValueError("HSL color must be a tuple of length 3!")

        # Convert HSL values to RGB
        if s == 0:
            r, g, b = l * 255, l * 255, l * 255
        else:
            c = (1 - abs(2 * l - 1)) * s
            x = c * (1 - abs((h / 60) % 2 - 1))
            m = l - c / 2
            if 0 <= h < 60:
                r, g, b = c, x, m
            elif 60 <= h < 120:
                r, g, b = x, c, m
            elif 120 <= h < 180:
                r, g, b = m, c, x
            elif 180 <= h < 240:
                r, g, b = m, x, c
            elif 240 <= h < 300:
                r, g, b = x, m, c
            else:
                r, g, b = c, m, x
        return int(r * 255), int(g * 255), int(b * 255)

    def to_hex(self, h, s=None, l=None):
        """
        Convert HSL color to HEX color.

        Args:
            h: Hue value in the range of 0 to 360.
            s: Saturation value in the range of 0.0 to 1.0. Optional.
            l: Lightness value in the range of 0.0 to 1.0. Optional.

        Returns:
            A tuple of HEX values.

        Examples:
            >>> HSLColor.to_hex(0.0, 1.0, 0.5)
            '#FF0000'
        """
        if s is None:
            s, l = h[1], h[2]
            h = h[0]
        return RGBColor.to_hex(HSLColor.to_rgb(h, s, l))


HSLColor = _HSLColor()

if __name__ == "__main__":
    doctest.testmod(verbose=True)
