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
New feature: gamehelper.game_help_window

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
"""
import os
import sys
import unittest

from pyhelper.constant import Constant, ConstantError

__version__ = '2.2.0'
__all__ = [
    'get_version',
    'RGBAColor',
    'HEXColor'
]

_PYTHON_PATH = sys.executable[:-11]
if os.name == 'nt' and _PYTHON_PATH[-6:] == 'Script':
    _PYTHON_PATH = _PYTHON_PATH[:-7]
elif os.name == 'posix' and _PYTHON_PATH[-3:] == 'bin':
    _PYTHON_PATH = _PYTHON_PATH[:-4]
_PYTHON_PATH = os.path.join(_PYTHON_PATH, 'Lib', 'site-packages', 'pyhelper')

if __name__ != '__main__':
    print(f'PyHelper {__version__}', end=' ')
    if os.name == 'nt':
        print(f'(Microsoft Windows,', end=' ')
    elif os.name == 'posix':
        print(f'(Unix,', end=' ')
    print(f'Python {sys.version_info[0]}.{sys.version_info[1]}.', end='')
    print(f'{sys.version_info[2]})')
    print(f'Hello, {os.getlogin()}!')
    print('Welcome to the PyHelper community!', end=' ')
    print('https://githun.com/nanocode38/pyhelper.git')


class _RGBColor:
    """
    A class about RGBA colors
    :function: to_css(rgbs: tuple) or to_css(rgbs: int, g: int, b: int, a: int = 255) -> str
    """
    RGBAColorConst = Constant()

    RGBAColorConst.ALICEBLUE = (
        240,
        248,
        255,
        255,
    )
    RGBAColorConst.ANTIQUEWHITE = (
        250,
        235,
        215,
        255,
    )
    RGBAColorConst.ANTIQUEWHITE1 = (
        255,
        239,
        219,
        255,
    )
    RGBAColorConst.ANTIQUEWHITE2 = (
        238,
        223,
        204,
        255,
    )
    RGBAColorConst.ANTIQUEWHITE3 = (
        205,
        192,
        176,
        255,
    )
    RGBAColorConst.ANTIQUEWHITE4 = (
        139,
        131,
        120,
        255,
    )
    RGBAColorConst.AQUA = (
        0,
        255,
        255,
        255,
    )
    RGBAColorConst.AQUAMARINE = (
        127,
        255,
        212,
        255,
    )
    RGBAColorConst.AQUAMARINE2 = (
        118,
        238,
        198,
        255,
    )
    RGBAColorConst.AQUAMARINE3 = (
        102,
        205,
        170,
        255,
    )
    RGBAColorConst.AQUAMARINE4 = (
        69,
        139,
        116,
        255,
    )
    RGBAColorConst.AZURE = (
        240,
        255,
        255,
        255,
    )
    RGBAColorConst.AZURE2 = (
        224,
        238,
        238,
        255,
    )
    RGBAColorConst.AZURE3 = (
        193,
        205,
        205,
        255,
    )
    RGBAColorConst.AZURE4 = (
        131,
        139,
        139,
        255,
    )
    RGBAColorConst.BEIGE = (
        245,
        245,
        220,
        255,
    )
    RGBAColorConst.BISQUE = (
        255,
        228,
        196,
        255,
    )
    RGBAColorConst.BISQUE2 = (
        238,
        213,
        183,
        255,
    )
    RGBAColorConst.BISQUE3 = (
        205,
        183,
        158,
        255,
    )
    RGBAColorConst.BISQUE4 = (
        139,
        125,
        107,
        255,
    )
    RGBAColorConst.BLACK = (
        0,
        0,
        0,
        255,
    )
    RGBAColorConst.BLANCHEDALMOND = (
        255,
        235,
        205,
        255,
    )
    RGBAColorConst.BLUE = (
        0,
        0,
        255,
        255,
    )
    RGBAColorConst.BLUE2 = (
        0,
        0,
        238,
        255,
    )
    RGBAColorConst.BLUE3 = (
        0,
        0,
        205,
        255,
    )
    RGBAColorConst.BLUE4 = (
        0,
        0,
        139,
        255,
    )
    RGBAColorConst.BLUEVIOLET = (
        138,
        43,
        226,
        255,
    )
    RGBAColorConst.BROWN = (
        165,
        42,
        42,
        255,
    )
    RGBAColorConst.BROWN1 = (
        255,
        64,
        64,
        255,
    )
    RGBAColorConst.BROWN2 = (
        238,
        59,
        59,
        255,
    )
    RGBAColorConst.BROWN3 = (
        205,
        51,
        51,
        255,
    )
    RGBAColorConst.BROWN4 = (
        139,
        35,
        35,
        255,
    )
    RGBAColorConst.BURLYWOOD = (
        222,
        184,
        135,
        255,
    )
    RGBAColorConst.BURLYWOOD1 = (
        255,
        211,
        155,
        255,
    )
    RGBAColorConst.BURLYWOOD2 = (
        238,
        197,
        145,
        255,
    )
    RGBAColorConst.BURLYWOOD3 = (
        205,
        170,
        125,
        255,
    )
    RGBAColorConst.BURLYWOOD4 = (
        139,
        115,
        85,
        255,
    )
    RGBAColorConst.CADETBLUE = (
        95,
        158,
        160,
        255,
    )
    RGBAColorConst.CADETBLUE1 = (
        152,
        245,
        255,
        255,
    )
    RGBAColorConst.CADETBLUE2 = (
        142,
        229,
        238,
        255,
    )
    RGBAColorConst.CADETBLUE3 = (
        122,
        197,
        205,
        255,
    )
    RGBAColorConst.CADETBLUE4 = (
        83,
        134,
        139,
        255,
    )
    RGBAColorConst.CHARTREUSE = (
        127,
        255,
        0,
        255,
    )
    RGBAColorConst.CHARTREUSE2 = (
        118,
        238,
        0,
        255,
    )
    RGBAColorConst.CHARTREUSE3 = (
        102,
        205,
        0,
        255,
    )
    RGBAColorConst.CHARTREUSE4 = (
        69,
        139,
        0,
        255,
    )
    RGBAColorConst.CHOCOLATE = (
        210,
        105,
        30,
        255,
    )
    RGBAColorConst.CHOCOLATE1 = (
        255,
        127,
        36,
        255,
    )
    RGBAColorConst.CHOCOLATE2 = (
        238,
        118,
        33,
        255,
    )
    RGBAColorConst.CHOCOLATE3 = (
        205,
        102,
        29,
        255,
    )
    RGBAColorConst.CHOCOLATE4 = (
        139,
        69,
        19,
        255,
    )
    RGBAColorConst.CORAL = (
        255,
        127,
        80,
        255,
    )
    RGBAColorConst.CORAL1 = (
        255,
        114,
        86,
        255,
    )
    RGBAColorConst.CORAL2 = (
        238,
        106,
        80,
        255,
    )
    RGBAColorConst.CORAL3 = (
        205,
        91,
        69,
        255,
    )
    RGBAColorConst.CORAL4 = (
        139,
        62,
        47,
        255,
    )
    RGBAColorConst.CORNFLOWERBLUE = (
        100,
        149,
        237,
        255,
    )
    RGBAColorConst.CORNSILK = (
        255,
        248,
        220,
        255,
    )
    RGBAColorConst.CORNSILK2 = (
        238,
        232,
        205,
        255,
    )
    RGBAColorConst.CORNSILK3 = (
        205,
        200,
        177,
        255,
    )
    RGBAColorConst.CORNSILK4 = (
        139,
        136,
        120,
        255,
    )
    RGBAColorConst.CRIMSON = (
        220,
        20,
        60,
        255,
    )
    RGBAColorConst.CYAN2 = (
        0,
        238,
        238,
        255,
    )
    RGBAColorConst.CYAN3 = (
        0,
        205,
        205,
        255,
    )
    RGBAColorConst.CYAN4 = (
        0,
        139,
        139,
        255,
    )
    RGBAColorConst.DARK_GOLDENROD = (
        184,
        134,
        11,
        255,
    )
    RGBAColorConst.DARK_GOLDENROD1 = (
        255,
        185,
        15,
        255,
    )
    RGBAColorConst.DARK_GOLDENROD2 = (
        238,
        173,
        14,
        255,
    )
    RGBAColorConst.DARK_GOLDENROD3 = (
        205,
        149,
        12,
        255,
    )
    RGBAColorConst.DARK_GOLDENROD4 = (
        139,
        101,
        8,
        255,
    )
    RGBAColorConst.DARK_GRAY = (
        169,
        169,
        169,
        255,
    )
    RGBAColorConst.DARK_GREEN = (
        0,
        100,
        0,
        255,
    )
    RGBAColorConst.DARK_KHAKI = (
        189,
        183,
        107,
        255,
    )
    RGBAColorConst.DARK_MAGENTA = (
        139,
        0,
        139,
        255,
    )
    RGBAColorConst.DARK_OLIVEGREEN = (
        85,
        107,
        47,
        255,
    )
    RGBAColorConst.DARK_OLIVEGREEN1 = (
        202,
        255,
        112,
        255,
    )
    RGBAColorConst.DARK_OLIVEGREEN2 = (
        188,
        238,
        104,
        255,
    )
    RGBAColorConst.DARK_OLIVEGREEN3 = (
        162,
        205,
        90,
        255,
    )
    RGBAColorConst.DARK_OLIVEGREEN4 = (
        110,
        139,
        61,
        255,
    )
    RGBAColorConst.DARK_ORANGE = (
        255,
        140,
        0,
        255,
    )
    RGBAColorConst.DARK_ORANGE1 = (
        255,
        127,
        0,
        255,
    )
    RGBAColorConst.DARK_ORANGE2 = (
        238,
        118,
        0,
        255,
    )
    RGBAColorConst.DARK_ORANGE3 = (
        205,
        102,
        0,
        255,
    )
    RGBAColorConst.DARK_ORANGE4 = (
        139,
        69,
        0,
        255,
    )
    RGBAColorConst.DARK_ORCHID = (
        153,
        50,
        204,
        255,
    )
    RGBAColorConst.DARK_ORCHID1 = (
        191,
        62,
        255,
        255,
    )
    RGBAColorConst.DARK_ORCHID2 = (
        178,
        58,
        238,
        255,
    )
    RGBAColorConst.DARK_ORCHID3 = (
        154,
        50,
        205,
        255,
    )
    RGBAColorConst.DARK_ORCHID4 = (
        104,
        34,
        139,
        255,
    )
    RGBAColorConst.DARK_RED = (
        139,
        0,
        0,
        255,
    )
    RGBAColorConst.DARK_SALMON = (
        233,
        150,
        122,
        255,
    )
    RGBAColorConst.DARK_SEA_GREEN = (
        143,
        188,
        143,
        255,
    )
    RGBAColorConst.DARK_SEA_GREEN1 = (
        193,
        255,
        193,
        255,
    )
    RGBAColorConst.DARK_SEA_GREEN2 = (
        180,
        238,
        180,
        255,
    )
    RGBAColorConst.DARK_SEA_GREEN3 = (
        155,
        205,
        155,
        255,
    )
    RGBAColorConst.DARK_SEA_GREEN4 = (
        105,
        139,
        105,
        255,
    )
    RGBAColorConst.DARK_SLATEBLUE = (
        72,
        61,
        139,
        255,
    )
    RGBAColorConst.DARK_SLATEGRAY = (
        47,
        79,
        79,
        255,
    )
    RGBAColorConst.DARK_SLATEGRAY1 = (
        151,
        255,
        255,
        255,
    )
    RGBAColorConst.DARK_SLATEGRAY2 = (
        141,
        238,
        238,
        255,
    )
    RGBAColorConst.DARK_SLATEGRAY3 = (
        121,
        205,
        205,
        255,
    )
    RGBAColorConst.DARK_SLATEGRAY4 = (
        82,
        139,
        139,
        255,
    )
    RGBAColorConst.DARK_TURQUOISE = (
        0,
        206,
        209,
        255,
    )
    RGBAColorConst.DARK_VIOLET = (
        148,
        0,
        211,
        255,
    )
    RGBAColorConst.DEEP_PINK = (
        255,
        20,
        147,
        255,
    )
    RGBAColorConst.DEEP_PINK2 = (
        238,
        18,
        137,
        255,
    )
    RGBAColorConst.DEEP_PINK3 = (
        205,
        16,
        118,
        255,
    )
    RGBAColorConst.DEEP_PINK4 = (
        139,
        10,
        80,
        255,
    )
    RGBAColorConst.DEEP_SKYBLUE = (
        0,
        191,
        255,
        255,
    )
    RGBAColorConst.DEEP_SKYBLUE2 = (
        0,
        178,
        238,
        255,
    )
    RGBAColorConst.DEEP_SKYBLUE3 = (
        0,
        154,
        205,
        255,
    )
    RGBAColorConst.DEEP_SKYBLUE4 = (
        0,
        104,
        139,
        255,
    )
    RGBAColorConst.DIMGRAY = (
        105,
        105,
        105,
        255,
    )
    RGBAColorConst.DODGERBLUE = (
        30,
        144,
        255,
        255,
    )
    RGBAColorConst.DODGERBLUE2 = (
        28,
        134,
        238,
        255,
    )
    RGBAColorConst.DODGERBLUE3 = (
        24,
        116,
        205,
        255,
    )
    RGBAColorConst.DODGERBLUE4 = (
        16,
        78,
        139,
        255,
    )
    RGBAColorConst.FIRE_BRICK = (
        178,
        34,
        34,
        255,
    )
    RGBAColorConst.FIRE_BRICK1 = (
        255,
        48,
        48,
        255,
    )
    RGBAColorConst.FIRE_BRICK2 = (
        238,
        44,
        44,
        255,
    )
    RGBAColorConst.FIRE_BRICK3 = (
        205,
        38,
        38,
        255,
    )
    RGBAColorConst.FIRE_BRICK4 = (
        139,
        26,
        26,
        255,
    )
    RGBAColorConst.FLORALWHITE = (
        255,
        250,
        240,
        255,
    )
    RGBAColorConst.FORESTGREEN = (
        34,
        139,
        34,
        255,
    )
    RGBAColorConst.FUCHSIA = (
        255,
        0,
        255,
        255,
    )
    RGBAColorConst.GAINSBORO = (
        220,
        220,
        220,
        255,
    )
    RGBAColorConst.GHOSTWHITE = (
        248,
        248,
        255,
        255,
    )
    RGBAColorConst.GOLD = (
        255,
        215,
        0,
        255,
    )
    RGBAColorConst.GOLD2 = (
        238,
        201,
        0,
        255,
    )
    RGBAColorConst.GOLD3 = (
        205,
        173,
        0,
        255,
    )
    RGBAColorConst.GOLD4 = (
        139,
        117,
        0,
        255,
    )
    RGBAColorConst.GOLDENROD = (
        218,
        165,
        32,
        255,
    )
    RGBAColorConst.GOLDENROD1 = (
        255,
        193,
        37,
        255,
    )
    RGBAColorConst.GOLDENROD2 = (
        238,
        180,
        34,
        255,
    )
    RGBAColorConst.GOLDENROD3 = (
        205,
        155,
        29,
        255,
    )
    RGBAColorConst.GOLDENROD4 = (
        139,
        105,
        20,
        255,
    )
    RGBAColorConst.GRAY = (
        190,
        190,
        190,
        255,
    )
    RGBAColorConst.GRAY1 = (
        3,
        3,
        3,
        255,
    )
    RGBAColorConst.GRAY10 = (
        26,
        26,
        26,
        255,
    )
    RGBAColorConst.GRAY100 = (
        255,
        255,
        255,
        255,
    )
    RGBAColorConst.GRAY11 = (
        28,
        28,
        28,
        255,
    )
    RGBAColorConst.GRAY12 = (
        31,
        31,
        31,
        255,
    )
    RGBAColorConst.GRAY13 = (
        33,
        33,
        33,
        255,
    )
    RGBAColorConst.GRAY14 = (
        36,
        36,
        36,
        255,
    )
    RGBAColorConst.GRAY15 = (
        38,
        38,
        38,
        255,
    )
    RGBAColorConst.GRAY16 = (
        41,
        41,
        41,
        255,
    )
    RGBAColorConst.GRAY17 = (
        43,
        43,
        43,
        255,
    )
    RGBAColorConst.GRAY18 = (
        46,
        46,
        46,
        255,
    )
    RGBAColorConst.GRAY19 = (
        48,
        48,
        48,
        255,
    )
    RGBAColorConst.GRAY2 = (
        5,
        5,
        5,
        255,
    )
    RGBAColorConst.GRAY20 = (
        51,
        51,
        51,
        255,
    )
    RGBAColorConst.GRAY21 = (
        54,
        54,
        54,
        255,
    )
    RGBAColorConst.GRAY22 = (
        56,
        56,
        56,
        255,
    )
    RGBAColorConst.GRAY23 = (
        59,
        59,
        59,
        255,
    )
    RGBAColorConst.GRAY24 = (
        61,
        61,
        61,
        255,
    )
    RGBAColorConst.GRAY25 = (
        64,
        64,
        64,
        255,
    )
    RGBAColorConst.GRAY26 = (
        66,
        66,
        66,
        255,
    )
    RGBAColorConst.GRAY27 = (
        69,
        69,
        69,
        255,
    )
    RGBAColorConst.GRAY28 = (
        71,
        71,
        71,
        255,
    )
    RGBAColorConst.GRAY29 = (
        74,
        74,
        74,
        255,
    )
    RGBAColorConst.GRAY3 = (
        8,
        8,
        8,
        255,
    )
    RGBAColorConst.GRAY30 = (
        77,
        77,
        77,
        255,
    )
    RGBAColorConst.GRAY31 = (
        79,
        79,
        79,
        255,
    )
    RGBAColorConst.GRAY32 = (
        82,
        82,
        82,
        255,
    )
    RGBAColorConst.GRAY33 = (
        84,
        84,
        84,
        255,
    )
    RGBAColorConst.GRAY34 = (
        87,
        87,
        87,
        255,
    )
    RGBAColorConst.GRAY35 = (
        89,
        89,
        89,
        255,
    )
    RGBAColorConst.GRAY36 = (
        92,
        92,
        92,
        255,
    )
    RGBAColorConst.GRAY37 = (
        94,
        94,
        94,
        255,
    )
    RGBAColorConst.GRAY38 = (
        97,
        97,
        97,
        255,
    )
    RGBAColorConst.GRAY39 = (
        99,
        99,
        99,
        255,
    )
    RGBAColorConst.GRAY4 = (
        10,
        10,
        10,
        255,
    )
    RGBAColorConst.GRAY40 = (
        102,
        102,
        102,
        255,
    )
    RGBAColorConst.GRAY42 = (
        107,
        107,
        107,
        255,
    )
    RGBAColorConst.GRAY43 = (
        110,
        110,
        110,
        255,
    )
    RGBAColorConst.GRAY44 = (
        112,
        112,
        112,
        255,
    )
    RGBAColorConst.GRAY45 = (
        115,
        115,
        115,
        255,
    )
    RGBAColorConst.GRAY46 = (
        117,
        117,
        117,
        255,
    )
    RGBAColorConst.GRAY47 = (
        120,
        120,
        120,
        255,
    )
    RGBAColorConst.GRAY48 = (
        122,
        122,
        122,
        255,
    )
    RGBAColorConst.GRAY49 = (
        125,
        125,
        125,
        255,
    )
    RGBAColorConst.GRAY5 = (
        13,
        13,
        13,
        255,
    )
    RGBAColorConst.GRAY50 = (
        127,
        127,
        127,
        255,
    )
    RGBAColorConst.GRAY51 = (
        130,
        130,
        130,
        255,
    )
    RGBAColorConst.GRAY52 = (
        133,
        133,
        133,
        255,
    )
    RGBAColorConst.GRAY53 = (
        135,
        135,
        135,
        255,
    )
    RGBAColorConst.GRAY54 = (
        138,
        138,
        138,
        255,
    )
    RGBAColorConst.GRAY55 = (
        140,
        140,
        140,
        255,
    )
    RGBAColorConst.GRAY56 = (
        143,
        143,
        143,
        255,
    )
    RGBAColorConst.GRAY57 = (
        145,
        145,
        145,
        255,
    )
    RGBAColorConst.GRAY58 = (
        148,
        148,
        148,
        255,
    )
    RGBAColorConst.GRAY59 = (
        150,
        150,
        150,
        255,
    )
    RGBAColorConst.GRAY6 = (
        15,
        15,
        15,
        255,
    )
    RGBAColorConst.GRAY60 = (
        153,
        153,
        153,
        255,
    )
    RGBAColorConst.GRAY61 = (
        156,
        156,
        156,
        255,
    )
    RGBAColorConst.GRAY62 = (
        158,
        158,
        158,
        255,
    )
    RGBAColorConst.GRAY63 = (
        161,
        161,
        161,
        255,
    )
    RGBAColorConst.GRAY64 = (
        163,
        163,
        163,
        255,
    )
    RGBAColorConst.GRAY65 = (
        166,
        166,
        166,
        255,
    )
    RGBAColorConst.GRAY66 = (
        168,
        168,
        168,
        255,
    )
    RGBAColorConst.GRAY67 = (
        171,
        171,
        171,
        255,
    )
    RGBAColorConst.GRAY68 = (
        173,
        173,
        173,
        255,
    )
    RGBAColorConst.GRAY69 = (
        176,
        176,
        176,
        255,
    )
    RGBAColorConst.GRAY7 = (
        18,
        18,
        18,
        255,
    )
    RGBAColorConst.GRAY70 = (
        179,
        179,
        179,
        255,
    )
    RGBAColorConst.GRAY71 = (
        181,
        181,
        181,
        255,
    )
    RGBAColorConst.GRAY72 = (
        184,
        184,
        184,
        255,
    )
    RGBAColorConst.GRAY73 = (
        186,
        186,
        186,
        255,
    )
    RGBAColorConst.GRAY74 = (
        189,
        189,
        189,
        255,
    )
    RGBAColorConst.GRAY75 = (
        191,
        191,
        191,
        255,
    )
    RGBAColorConst.GRAY76 = (
        194,
        194,
        194,
        255,
    )
    RGBAColorConst.GRAY77 = (
        196,
        196,
        196,
        255,
    )
    RGBAColorConst.GRAY78 = (
        199,
        199,
        199,
        255,
    )
    RGBAColorConst.GRAY79 = (
        201,
        201,
        201,
        255,
    )
    RGBAColorConst.GRAY8 = (
        20,
        20,
        20,
        255,
    )
    RGBAColorConst.GRAY80 = (
        204,
        204,
        204,
        255,
    )
    RGBAColorConst.GRAY81 = (
        207,
        207,
        207,
        255,
    )
    RGBAColorConst.GRAY82 = (
        209,
        209,
        209,
        255,
    )
    RGBAColorConst.GRAY83 = (
        212,
        212,
        212,
        255,
    )
    RGBAColorConst.GRAY84 = (
        214,
        214,
        214,
        255,
    )
    RGBAColorConst.GRAY85 = (
        217,
        217,
        217,
        255,
    )
    RGBAColorConst.GRAY86 = (
        219,
        219,
        219,
        255,
    )
    RGBAColorConst.GRAY87 = (
        222,
        222,
        222,
        255,
    )
    RGBAColorConst.GRAY88 = (
        224,
        224,
        224,
        255,
    )
    RGBAColorConst.GRAY89 = (
        227,
        227,
        227,
        255,
    )
    RGBAColorConst.GRAY9 = (
        23,
        23,
        23,
        255,
    )
    RGBAColorConst.GRAY90 = (
        229,
        229,
        229,
        255,
    )
    RGBAColorConst.GRAY91 = (
        232,
        232,
        232,
        255,
    )
    RGBAColorConst.GRAY92 = (
        235,
        235,
        235,
        255,
    )
    RGBAColorConst.GRAY93 = (
        237,
        237,
        237,
        255,
    )
    RGBAColorConst.GRAY94 = (
        240,
        240,
        240,
        255,
    )
    RGBAColorConst.GRAY95 = (
        242,
        242,
        242,
        255,
    )
    RGBAColorConst.GRAY96 = (
        245,
        245,
        245,
        255,
    )
    RGBAColorConst.GRAY97 = (
        247,
        247,
        247,
        255,
    )
    RGBAColorConst.GRAY98 = (
        250,
        250,
        250,
        255,
    )
    RGBAColorConst.GRAY99 = (
        252,
        252,
        252,
        255,
    )
    RGBAColorConst.GREEN = (
        0,
        255,
        0,
        255,
    )
    RGBAColorConst.GREEN2 = (
        0,
        238,
        0,
        255,
    )
    RGBAColorConst.GREEN3 = (
        0,
        205,
        0,
        255,
    )
    RGBAColorConst.GREEN4 = (
        0,
        139,
        0,
        255,
    )
    RGBAColorConst.GREENYELLOW = (
        173,
        255,
        47,
        255,
    )
    RGBAColorConst.HONEYDEW = (
        240,
        255,
        240,
        255,
    )
    RGBAColorConst.HONEYDEW2 = (
        224,
        238,
        224,
        255,
    )
    RGBAColorConst.HONEYDEW3 = (
        193,
        205,
        193,
        255,
    )
    RGBAColorConst.HONEYDEW4 = (
        131,
        139,
        131,
        255,
    )
    RGBAColorConst.HOT_PINK = (
        255,
        105,
        180,
        255,
    )
    RGBAColorConst.HOT_PINK1 = (
        255,
        110,
        180,
        255,
    )
    RGBAColorConst.HOT_PINK2 = (
        238,
        106,
        167,
        255,
    )
    RGBAColorConst.HOT_PINK3 = (
        205,
        96,
        144,
        255,
    )
    RGBAColorConst.HOT_PINK4 = (
        139,
        58,
        98,
        255,
    )
    RGBAColorConst.INDIANRED = (
        205,
        92,
        92,
        255,
    )
    RGBAColorConst.INDIANRED1 = (
        255,
        106,
        106,
        255,
    )
    RGBAColorConst.INDIANRED2 = (
        238,
        99,
        99,
        255,
    )
    RGBAColorConst.INDIANRED3 = (
        205,
        85,
        85,
        255,
    )
    RGBAColorConst.INDIANRED4 = (
        139,
        58,
        58,
        255,
    )
    RGBAColorConst.INDIGO = (
        75,
        0,
        130,
        255,
    )
    RGBAColorConst.IVORY = (
        255,
        255,
        240,
        255,
    )
    RGBAColorConst.IVORY2 = (
        238,
        238,
        224,
        255,
    )
    RGBAColorConst.IVORY3 = (
        205,
        205,
        193,
        255,
    )
    RGBAColorConst.IVORY4 = (
        139,
        139,
        131,
        255,
    )
    RGBAColorConst.KHAKI = (
        240,
        230,
        140,
        255,
    )
    RGBAColorConst.KHAKI1 = (
        255,
        246,
        143,
        255,
    )
    RGBAColorConst.KHAKI2 = (
        238,
        230,
        133,
        255,
    )
    RGBAColorConst.KHAKI3 = (
        205,
        198,
        115,
        255,
    )
    RGBAColorConst.KHAKI4 = (
        139,
        134,
        78,
        255,
    )
    RGBAColorConst.LAVENDER = (
        230,
        230,
        250,
        255,
    )
    RGBAColorConst.LAVENDERBLUSH = (
        255,
        240,
        245,
        255,
    )
    RGBAColorConst.LAVENDERBLUSH2 = (
        238,
        224,
        229,
        255,
    )
    RGBAColorConst.LAVENDERBLUSH3 = (
        205,
        193,
        197,
        255,
    )
    RGBAColorConst.LAVENDERBLUSH4 = (
        139,
        131,
        134,
        255,
    )
    RGBAColorConst.LAWNGREEN = (
        124,
        252,
        0,
        255,
    )
    RGBAColorConst.LEMONCHIFFON = (
        255,
        250,
        205,
        255,
    )
    RGBAColorConst.LEMONCHIFFON2 = (
        238,
        233,
        191,
        255,
    )
    RGBAColorConst.LEMONCHIFFON3 = (
        205,
        201,
        165,
        255,
    )
    RGBAColorConst.LEMONCHIFFON4 = (
        139,
        137,
        112,
        255,
    )
    RGBAColorConst.LIGHT_BLUE = (
        173,
        216,
        230,
        255,
    )
    RGBAColorConst.LIGHT_BLUE1 = (
        191,
        239,
        255,
        255,
    )
    RGBAColorConst.LIGHT_BLUE2 = (
        178,
        223,
        238,
        255,
    )
    RGBAColorConst.LIGHT_BLUE3 = (
        154,
        192,
        205,
        255,
    )
    RGBAColorConst.LIGHT_BLUE4 = (
        104,
        131,
        139,
        255,
    )
    RGBAColorConst.LIGHT_CORAL = (
        240,
        128,
        128,
        255,
    )
    RGBAColorConst.LIGHT_CYAN = (
        224,
        255,
        255,
        255,
    )
    RGBAColorConst.LIGHT_CYAN2 = (
        209,
        238,
        238,
        255,
    )
    RGBAColorConst.LIGHT_CYAN3 = (
        180,
        205,
        205,
        255,
    )
    RGBAColorConst.LIGHT_CYAN4 = (
        122,
        139,
        139,
        255,
    )
    RGBAColorConst.LIGHT_GOLDENROD = (
        238,
        221,
        130,
        255,
    )
    RGBAColorConst.LIGHT_GOLDENROD1 = (
        255,
        236,
        139,
        255,
    )
    RGBAColorConst.LIGHT_GOLDENROD2 = (
        238,
        220,
        130,
        255,
    )
    RGBAColorConst.LIGHT_GOLDENROD3 = (
        205,
        190,
        112,
        255,
    )
    RGBAColorConst.LIGHT_GOLDENROD4 = (
        139,
        129,
        76,
        255,
    )
    RGBAColorConst.LIGHT_GOLDENRODYELLOW = (
        250,
        250,
        210,
        255,
    )
    RGBAColorConst.LIGHT_GRAY = (
        211,
        211,
        211,
        255,
    )
    RGBAColorConst.LIGHT_GREEN = (
        144,
        238,
        144,
        255,
    )
    RGBAColorConst.LIGHT_PINK = (
        255,
        182,
        193,
        255,
    )
    RGBAColorConst.LIGHT_PINK1 = (
        255,
        174,
        185,
        255,
    )
    RGBAColorConst.LIGHT_PINK2 = (
        238,
        162,
        173,
        255,
    )
    RGBAColorConst.LIGHT_PINK3 = (
        205,
        140,
        149,
        255,
    )
    RGBAColorConst.LIGHT_PINK4 = (
        139,
        95,
        101,
        255,
    )
    RGBAColorConst.LIGHT_SALMON = (
        255,
        160,
        122,
        255,
    )
    RGBAColorConst.LIGHT_SALMON2 = (
        238,
        149,
        114,
        255,
    )
    RGBAColorConst.LIGHT_SALMON3 = (
        205,
        129,
        98,
        255,
    )
    RGBAColorConst.LIGHT_SALMON4 = (
        139,
        87,
        66,
        255,
    )
    RGBAColorConst.LIGHT_SEA_GREEN = (
        32,
        178,
        170,
        255,
    )
    RGBAColorConst.LIGHT_SKYBLUE = (
        135,
        206,
        250,
        255,
    )
    RGBAColorConst.LIGHT_SKYBLUE1 = (
        176,
        226,
        255,
        255,
    )
    RGBAColorConst.LIGHT_SKYBLUE2 = (
        164,
        211,
        238,
        255,
    )
    RGBAColorConst.LIGHT_SKYBLUE3 = (
        141,
        182,
        205,
        255,
    )
    RGBAColorConst.LIGHT_SKYBLUE4 = (
        96,
        123,
        139,
        255,
    )
    RGBAColorConst.LIGHT_SLATEBLUE = (
        132,
        112,
        255,
        255,
    )
    RGBAColorConst.LIGHT_SLATEGRAY = (
        119,
        136,
        153,
        255,
    )
    RGBAColorConst.LIGHT_STEELBLUE = (
        176,
        196,
        222,
        255,
    )
    RGBAColorConst.LIGHT_STEELBLUE1 = (
        202,
        225,
        255,
        255,
    )
    RGBAColorConst.LIGHT_STEELBLUE2 = (
        188,
        210,
        238,
        255,
    )
    RGBAColorConst.LIGHT_STEELBLUE3 = (
        162,
        181,
        205,
        255,
    )
    RGBAColorConst.LIGHT_STEELBLUE4 = (
        110,
        123,
        139,
        255,
    )
    RGBAColorConst.LIGHT_YELLOW = (
        255,
        255,
        224,
        255,
    )
    RGBAColorConst.LIGHT_YELLOW2 = (
        238,
        238,
        209,
        255,
    )
    RGBAColorConst.LIGHT_YELLOW3 = (
        205,
        205,
        180,
        255,
    )
    RGBAColorConst.LIGHT_YELLOW4 = (
        139,
        139,
        122,
        255,
    )
    RGBAColorConst.LIME_GREEN = (
        50,
        205,
        50,
        255,
    )
    RGBAColorConst.LINEN = (
        250,
        240,
        230,
        255,
    )
    RGBAColorConst.MAGENTA2 = (
        238,
        0,
        238,
        255,
    )
    RGBAColorConst.MAGENTA3 = (
        205,
        0,
        205,
        255,
    )
    RGBAColorConst.MAROON = (
        176,
        48,
        96,
        255,
    )
    RGBAColorConst.MAROON1 = (
        255,
        52,
        179,
        255,
    )
    RGBAColorConst.MAROON2 = (
        238,
        48,
        167,
        255,
    )
    RGBAColorConst.MAROON3 = (
        205,
        41,
        144,
        255,
    )
    RGBAColorConst.MAROON4 = (
        139,
        28,
        98,
        255,
    )
    RGBAColorConst.MEDIUM_ORCHID = (
        186,
        85,
        211,
        255,
    )
    RGBAColorConst.MEDIUM_ORCHID1 = (
        224,
        102,
        255,
        255,
    )
    RGBAColorConst.MEDIUM_ORCHID2 = (
        209,
        95,
        238,
        255,
    )
    RGBAColorConst.MEDIUM_ORCHID3 = (
        180,
        82,
        205,
        255,
    )
    RGBAColorConst.MEDIUM_ORCHID4 = (
        122,
        55,
        139,
        255,
    )
    RGBAColorConst.MEDIUM_PURPLE = (
        147,
        112,
        219,
        255,
    )
    RGBAColorConst.MEDIUM_PURPLE1 = (
        171,
        130,
        255,
        255,
    )
    RGBAColorConst.MEDIUM_PURPLE2 = (
        159,
        121,
        238,
        255,
    )
    RGBAColorConst.MEDIUM_PURPLE3 = (
        137,
        104,
        205,
        255,
    )
    RGBAColorConst.MEDIUM_PURPLE4 = (
        93,
        71,
        139,
        255,
    )
    RGBAColorConst.MEDIUM_SEA_GREEN = (
        60,
        179,
        113,
        255,
    )
    RGBAColorConst.MEDIUM_SLATEBLUE = (
        123,
        104,
        238,
        255,
    )
    RGBAColorConst.MEDIUM_SPRINGGREEN = (
        0,
        250,
        154,
        255,
    )
    RGBAColorConst.MEDIUM_TURQUOISE = (
        72,
        209,
        204,
        255,
    )
    RGBAColorConst.MEDIUM_VIOLETRED = (
        199,
        21,
        133,
        255,
    )
    RGBAColorConst.MIDNIGHTBLUE = (
        25,
        25,
        112,
        255,
    )
    RGBAColorConst.MINTCREAM = (
        245,
        255,
        250,
        255,
    )
    RGBAColorConst.MISTYROSE = (
        255,
        228,
        225,
        255,
    )
    RGBAColorConst.MISTYROSE2 = (
        238,
        213,
        210,
        255,
    )
    RGBAColorConst.MISTYROSE3 = (
        205,
        183,
        181,
        255,
    )
    RGBAColorConst.MISTYROSE4 = (
        139,
        125,
        123,
        255,
    )
    RGBAColorConst.MOCCASIN = (
        255,
        228,
        181,
        255,
    )
    RGBAColorConst.NAVAJOWHITE = (
        255,
        222,
        173,
        255,
    )
    RGBAColorConst.NAVAJOWHITE2 = (
        238,
        207,
        161,
        255,
    )
    RGBAColorConst.NAVAJOWHITE3 = (
        205,
        179,
        139,
        255,
    )
    RGBAColorConst.NAVAJOWHITE4 = (
        139,
        121,
        94,
        255,
    )
    RGBAColorConst.NAVY = (
        0,
        0,
        128,
        255,
    )
    RGBAColorConst.OLDLACE = (
        253,
        245,
        230,
        255,
    )
    RGBAColorConst.OLIVE = (
        128,
        128,
        0,
        255,
    )
    RGBAColorConst.OLIVEDRAB = (
        107,
        142,
        35,
        255,
    )
    RGBAColorConst.OLIVEDRAB1 = (
        192,
        255,
        62,
        255,
    )
    RGBAColorConst.OLIVEDRAB2 = (
        179,
        238,
        58,
        255,
    )
    RGBAColorConst.OLIVEDRAB3 = (
        154,
        205,
        50,
        255,
    )
    RGBAColorConst.OLIVEDRAB4 = (
        105,
        139,
        34,
        255,
    )
    RGBAColorConst.ORANGE = (
        255,
        165,
        0,
        255,
    )
    RGBAColorConst.ORANGE2 = (
        238,
        154,
        0,
        255,
    )
    RGBAColorConst.ORANGE3 = (
        205,
        133,
        0,
        255,
    )
    RGBAColorConst.ORANGE4 = (
        139,
        90,
        0,
        255,
    )
    RGBAColorConst.ORANGERED = (
        255,
        69,
        0,
        255,
    )
    RGBAColorConst.ORANGERED2 = (
        238,
        64,
        0,
        255,
    )
    RGBAColorConst.ORANGERED3 = (
        205,
        55,
        0,
        255,
    )
    RGBAColorConst.ORANGERED4 = (
        139,
        37,
        0,
        255,
    )
    RGBAColorConst.ORCHID = (
        218,
        112,
        214,
        255,
    )
    RGBAColorConst.ORCHID1 = (
        255,
        131,
        250,
        255,
    )
    RGBAColorConst.ORCHID2 = (
        238,
        122,
        233,
        255,
    )
    RGBAColorConst.ORCHID3 = (
        205,
        105,
        201,
        255,
    )
    RGBAColorConst.ORCHID4 = (
        139,
        71,
        137,
        255,
    )
    RGBAColorConst.PALE_GOLDENROD = (
        238,
        232,
        170,
        255,
    )
    RGBAColorConst.PALE_GREEN = (
        152,
        251,
        152,
        255,
    )
    RGBAColorConst.PALE_GREEN1 = (
        154,
        255,
        154,
        255,
    )
    RGBAColorConst.PALE_GREEN3 = (
        124,
        205,
        124,
        255,
    )
    RGBAColorConst.PALE_GREEN4 = (
        84,
        139,
        84,
        255,
    )
    RGBAColorConst.PALE_TURQUOISE = (
        175,
        238,
        238,
        255,
    )
    RGBAColorConst.PALE_TURQUOISE1 = (
        187,
        255,
        255,
        255,
    )
    RGBAColorConst.PALE_TURQUOISE2 = (
        174,
        238,
        238,
        255,
    )
    RGBAColorConst.PALE_TURQUOISE3 = (
        150,
        205,
        205,
        255,
    )
    RGBAColorConst.PALE_TURQUOISE4 = (
        102,
        139,
        139,
        255,
    )
    RGBAColorConst.PALE_VIOLETRED = (
        219,
        112,
        147,
        255,
    )
    RGBAColorConst.PALE_VIOLETRED1 = (
        255,
        130,
        171,
        255,
    )
    RGBAColorConst.PALE_VIOLETRED2 = (
        238,
        121,
        159,
        255,
    )
    RGBAColorConst.PALE_VIOLETRED3 = (
        205,
        104,
        137,
        255,
    )
    RGBAColorConst.PALE_VIOLETRED4 = (
        139,
        71,
        93,
        255,
    )
    RGBAColorConst.PAPAYAWHIP = (
        255,
        239,
        213,
        255,
    )
    RGBAColorConst.PEACHPUFF = (
        255,
        218,
        185,
        255,
    )
    RGBAColorConst.PEACHPUFF2 = (
        238,
        203,
        173,
        255,
    )
    RGBAColorConst.PEACHPUFF3 = (
        205,
        175,
        149,
        255,
    )
    RGBAColorConst.PEACHPUFF4 = (
        139,
        119,
        101,
        255,
    )
    RGBAColorConst.PERU = (
        205,
        133,
        63,
        255,
    )
    RGBAColorConst.PINK = (
        255,
        192,
        203,
        255,
    )
    RGBAColorConst.PINK1 = (
        255,
        181,
        197,
        255,
    )
    RGBAColorConst.PINK2 = (
        238,
        169,
        184,
        255,
    )
    RGBAColorConst.PINK3 = (
        205,
        145,
        158,
        255,
    )
    RGBAColorConst.PINK4 = (
        139,
        99,
        108,
        255,
    )
    RGBAColorConst.PLUM = (
        221,
        160,
        221,
        255,
    )
    RGBAColorConst.PLUM1 = (
        255,
        187,
        255,
        255,
    )
    RGBAColorConst.PLUM2 = (
        238,
        174,
        238,
        255,
    )
    RGBAColorConst.PLUM3 = (
        205,
        150,
        205,
        255,
    )
    RGBAColorConst.PLUM4 = (
        139,
        102,
        139,
        255,
    )
    RGBAColorConst.POWDERBLUE = (
        176,
        224,
        230,
        255,
    )
    RGBAColorConst.PURPLE = (
        160,
        32,
        240,
        255,
    )
    RGBAColorConst.PURPLE1 = (
        155,
        48,
        255,
        255,
    )
    RGBAColorConst.PURPLE2 = (
        145,
        44,
        238,
        255,
    )
    RGBAColorConst.PURPLE3 = (
        125,
        38,
        205,
        255,
    )
    RGBAColorConst.PURPLE4 = (
        85,
        26,
        139,
        255,
    )
    RGBAColorConst.RED = (
        255,
        0,
        0,
        255,
    )
    RGBAColorConst.RED2 = (
        238,
        0,
        0,
        255,
    )
    RGBAColorConst.RED3 = (
        205,
        0,
        0,
        255,
    )
    RGBAColorConst.ROSYBROWN = (
        188,
        143,
        143,
        255,
    )
    RGBAColorConst.ROSYBROWN1 = (
        255,
        193,
        193,
        255,
    )
    RGBAColorConst.ROSYBROWN2 = (
        238,
        180,
        180,
        255,
    )
    RGBAColorConst.ROSYBROWN3 = (
        205,
        155,
        155,
        255,
    )
    RGBAColorConst.ROSYBROWN4 = (
        139,
        105,
        105,
        255,
    )
    RGBAColorConst.ROYALBLUE = (
        65,
        105,
        225,
        255,
    )
    RGBAColorConst.ROYALBLUE1 = (
        72,
        118,
        255,
        255,
    )
    RGBAColorConst.ROYALBLUE2 = (
        67,
        110,
        238,
        255,
    )
    RGBAColorConst.ROYALBLUE3 = (
        58,
        95,
        205,
        255,
    )
    RGBAColorConst.ROYALBLUE4 = (
        39,
        64,
        139,
        255,
    )
    RGBAColorConst.SALMON = (
        250,
        128,
        114,
        255,
    )
    RGBAColorConst.SALMON1 = (
        255,
        140,
        105,
        255,
    )
    RGBAColorConst.SALMON2 = (
        238,
        130,
        98,
        255,
    )
    RGBAColorConst.SALMON3 = (
        205,
        112,
        84,
        255,
    )
    RGBAColorConst.SALMON4 = (
        139,
        76,
        57,
        255,
    )
    RGBAColorConst.SANDYBROWN = (
        244,
        164,
        96,
        255,
    )
    RGBAColorConst.SEA_GREEN = (
        46,
        139,
        87,
        255,
    )
    RGBAColorConst.SEA_GREEN1 = (
        84,
        255,
        159,
        255,
    )
    RGBAColorConst.SEA_GREEN2 = (
        78,
        238,
        148,
        255,
    )
    RGBAColorConst.SEA_GREEN3 = (
        67,
        205,
        128,
        255,
    )
    RGBAColorConst.SEA_SHELL = (
        255,
        245,
        238,
        255,
    )
    RGBAColorConst.SEA_SHELL2 = (
        238,
        229,
        222,
        255,
    )
    RGBAColorConst.SEA_SHELL3 = (
        205,
        197,
        191,
        255,
    )
    RGBAColorConst.SEA_SHELL4 = (
        139,
        134,
        130,
        255,
    )
    RGBAColorConst.SIENNA = (
        160,
        82,
        45,
        255,
    )
    RGBAColorConst.SIENNA1 = (
        255,
        130,
        71,
        255,
    )
    RGBAColorConst.SIENNA2 = (
        238,
        121,
        66,
        255,
    )
    RGBAColorConst.SIENNA3 = (
        205,
        104,
        57,
        255,
    )
    RGBAColorConst.SIENNA4 = (
        139,
        71,
        38,
        255,
    )
    RGBAColorConst.SILVER = (
        192,
        192,
        192,
        255,
    )
    RGBAColorConst.SKYBLUE = (
        135,
        206,
        235,
        255,
    )
    RGBAColorConst.SKYBLUE1 = (
        135,
        206,
        255,
        255,
    )
    RGBAColorConst.SKYBLUE2 = (
        126,
        192,
        238,
        255,
    )
    RGBAColorConst.SKYBLUE3 = (
        108,
        166,
        205,
        255,
    )
    RGBAColorConst.SKYBLUE4 = (
        74,
        112,
        139,
        255,
    )
    RGBAColorConst.SLATEBLUE = (
        106,
        90,
        205,
        255,
    )
    RGBAColorConst.SLATEBLUE1 = (
        131,
        111,
        255,
        255,
    )
    RGBAColorConst.SLATEBLUE2 = (
        122,
        103,
        238,
        255,
    )
    RGBAColorConst.SLATEBLUE3 = (
        105,
        89,
        205,
        255,
    )
    RGBAColorConst.SLATEBLUE4 = (
        71,
        60,
        139,
        255,
    )
    RGBAColorConst.SLATEGRAY = (
        112,
        128,
        144,
        255,
    )
    RGBAColorConst.SLATEGRAY1 = (
        198,
        226,
        255,
        255,
    )
    RGBAColorConst.SLATEGRAY2 = (
        185,
        211,
        238,
        255,
    )
    RGBAColorConst.SLATEGRAY3 = (
        159,
        182,
        205,
        255,
    )
    RGBAColorConst.SLATEGRAY4 = (
        108,
        123,
        139,
        255,
    )
    RGBAColorConst.SNOW = (
        255,
        250,
        250,
        255,
    )
    RGBAColorConst.SNOW2 = (
        238,
        233,
        233,
        255,
    )
    RGBAColorConst.SNOW3 = (
        205,
        201,
        201,
        255,
    )
    RGBAColorConst.SNOW4 = (
        139,
        137,
        137,
        255,
    )
    RGBAColorConst.SPRINGGREEN = (
        0,
        255,
        127,
        255,
    )
    RGBAColorConst.SPRINGGREEN2 = (
        0,
        238,
        118,
        255,
    )
    RGBAColorConst.SPRINGGREEN3 = (
        0,
        205,
        102,
        255,
    )
    RGBAColorConst.SPRINGGREEN4 = (
        0,
        139,
        69,
        255,
    )
    RGBAColorConst.STEELBLUE = (
        70,
        130,
        180,
        255,
    )
    RGBAColorConst.STEELBLUE1 = (
        99,
        184,
        255,
        255,
    )
    RGBAColorConst.STEELBLUE2 = (
        92,
        172,
        238,
        255,
    )
    RGBAColorConst.STEELBLUE3 = (
        79,
        148,
        205,
        255,
    )
    RGBAColorConst.STEELBLUE4 = (
        54,
        100,
        139,
        255,
    )
    RGBAColorConst.TAN = (
        210,
        180,
        140,
        255,
    )
    RGBAColorConst.TAN1 = (
        255,
        165,
        79,
        255,
    )
    RGBAColorConst.TAN2 = (
        238,
        154,
        73,
        255,
    )
    RGBAColorConst.TAN4 = (
        139,
        90,
        43,
        255,
    )
    RGBAColorConst.TEAL = (
        0,
        128,
        128,
        255,
    )
    RGBAColorConst.THISTLE = (
        216,
        191,
        216,
        255,
    )
    RGBAColorConst.THISTLE1 = (
        255,
        225,
        255,
        255,
    )
    RGBAColorConst.THISTLE2 = (
        238,
        210,
        238,
        255,
    )
    RGBAColorConst.THISTLE3 = (
        205,
        181,
        205,
        255,
    )
    RGBAColorConst.THISTLE4 = (
        139,
        123,
        139,
        255,
    )
    RGBAColorConst.TOMATO = (
        255,
        99,
        71,
        255,
    )
    RGBAColorConst.TOMATO2 = (
        238,
        92,
        66,
        255,
    )
    RGBAColorConst.TOMATO3 = (
        205,
        79,
        57,
        255,
    )
    RGBAColorConst.TOMATO4 = (
        139,
        54,
        38,
        255,
    )
    RGBAColorConst.TURQUOISE = (
        64,
        224,
        208,
        255,
    )
    RGBAColorConst.TURQUOISE1 = (
        0,
        245,
        255,
        255,
    )
    RGBAColorConst.TURQUOISE2 = (
        0,
        229,
        238,
        255,
    )
    RGBAColorConst.TURQUOISE3 = (
        0,
        197,
        205,
        255,
    )
    RGBAColorConst.TURQUOISE4 = (
        0,
        134,
        139,
        255,
    )
    RGBAColorConst.VIOLET = (
        238,
        130,
        238,
        255,
    )
    RGBAColorConst.VIOLETRED = (
        208,
        32,
        144,
        255,
    )
    RGBAColorConst.VIOLETRED1 = (
        255,
        62,
        150,
        255,
    )
    RGBAColorConst.VIOLETRED2 = (
        238,
        58,
        140,
        255,
    )
    RGBAColorConst.VIOLETRED3 = (
        205,
        50,
        120,
        255,
    )
    RGBAColorConst.VIOLETRED4 = (
        139,
        34,
        82,
        255,
    )
    RGBAColorConst.WHEAT = (
        245,
        222,
        179,
        255,
    )
    RGBAColorConst.WHEAT1 = (
        255,
        231,
        186,
        255,
    )
    RGBAColorConst.WHEAT2 = (
        238,
        216,
        174,
        255,
    )
    RGBAColorConst.WHEAT3 = (
        205,
        186,
        150,
        255,
    )
    RGBAColorConst.WHEAT4 = (
        139,
        126,
        102,
        255,
    )
    RGBAColorConst.WHITE = (
        255,
        255,
        255,
        255
    )
    RGBAColorConst.YELLOW = (
        255,
        255,
        0,
        255,
    )
    RGBAColorConst.YELLOW2 = (
        238,
        238,
        0,
        255,
    )
    RGBAColorConst.YELLOW3 = (
        205,
        205,
        0,
        255,
    )
    RGBAColorConst.YELLOW4 = (
        139,
        139,
        0,
        255,
    )

    @staticmethod
    def to_css(r, g=None, b=None, a=None) -> str:
        """
        Convert RGBA color tuple to CSS color string.

        :param r: RGBA Color.
        :param g: Optional. Third color component.
        :param b: Optional. Fourth color component.
        :param a: Optional. Fifth color component.
        :return string: CSS color string.
        """
        if g is None:
            g = r[1]
            b = r[2]
            try:
                a = r[3]
            except IndexError:
                a = 255
            r = r[0]
        elif a is None:
            a = 255
        return '#{:02X}{:02X}{:02X}{:02X}'.format(r, g, b, a).upper()


class _CSSColor:
    """
    A class about HEX colors
    """
    CSSColorConst = Constant()
    CSSColorConst.ALICEBLUE = _RGBColor.to_css(
        240,
        248,
        255,
        255,
    )
    CSSColorConst.ANTIQUEWHITE = _RGBColor.to_css(
        250,
        235,
        215,
        255,
    )
    CSSColorConst.ANTIQUEWHITE1 = _RGBColor.to_css(
        255,
        239,
        219,
        255,
    )
    CSSColorConst.ANTIQUEWHITE2 = _RGBColor.to_css(
        238,
        223,
        204,
        255,
    )
    CSSColorConst.ANTIQUEWHITE3 = _RGBColor.to_css(
        205,
        192,
        176,
        255,
    )
    CSSColorConst.ANTIQUEWHITE4 = _RGBColor.to_css(
        139,
        131,
        120,
        255,
    )
    CSSColorConst.AQUA = _RGBColor.to_css(
        0,
        255,
        255,
        255,
    )
    CSSColorConst.AQUAMARINE = _RGBColor.to_css(
        127,
        255,
        212,
        255,
    )
    CSSColorConst.AQUAMARINE2 = _RGBColor.to_css(
        118,
        238,
        198,
        255,
    )
    CSSColorConst.AQUAMARINE3 = _RGBColor.to_css(
        102,
        205,
        170,
        255,
    )
    CSSColorConst.AQUAMARINE4 = _RGBColor.to_css(
        69,
        139,
        116,
        255,
    )
    CSSColorConst.AZURE = _RGBColor.to_css(
        240,
        255,
        255,
        255,
    )
    CSSColorConst.AZURE2 = _RGBColor.to_css(
        224,
        238,
        238,
        255,
    )
    CSSColorConst.AZURE3 = _RGBColor.to_css(
        193,
        205,
        205,
        255,
    )
    CSSColorConst.AZURE4 = _RGBColor.to_css(
        131,
        139,
        139,
        255,
    )
    CSSColorConst.BEIGE = _RGBColor.to_css(
        245,
        245,
        220,
        255,
    )
    CSSColorConst.BISQUE = _RGBColor.to_css(
        255,
        228,
        196,
        255,
    )
    CSSColorConst.BISQUE2 = _RGBColor.to_css(
        238,
        213,
        183,
        255,
    )
    CSSColorConst.BISQUE3 = _RGBColor.to_css(
        205,
        183,
        158,
        255,
    )
    CSSColorConst.BISQUE4 = _RGBColor.to_css(
        139,
        125,
        107,
        255,
    )
    CSSColorConst.BLACK = _RGBColor.to_css(
        0,
        0,
        0,
        255,
    )
    CSSColorConst.BLANCHEDALMOND = _RGBColor.to_css(
        255,
        235,
        205,
        255,
    )
    CSSColorConst.BLUE = _RGBColor.to_css(
        0,
        0,
        255,
        255,
    )
    CSSColorConst.BLUE2 = _RGBColor.to_css(
        0,
        0,
        238,
        255,
    )
    CSSColorConst.BLUE3 = _RGBColor.to_css(
        0,
        0,
        205,
        255,
    )
    CSSColorConst.BLUE4 = _RGBColor.to_css(
        0,
        0,
        139,
        255,
    )
    CSSColorConst.BLUEVIOLET = _RGBColor.to_css(
        138,
        43,
        226,
        255,
    )
    CSSColorConst.BROWN = _RGBColor.to_css(
        165,
        42,
        42,
        255,
    )
    CSSColorConst.BROWN1 = _RGBColor.to_css(
        255,
        64,
        64,
        255,
    )
    CSSColorConst.BROWN2 = _RGBColor.to_css(
        238,
        59,
        59,
        255,
    )
    CSSColorConst.BROWN3 = _RGBColor.to_css(
        205,
        51,
        51,
        255,
    )
    CSSColorConst.BROWN4 = _RGBColor.to_css(
        139,
        35,
        35,
        255,
    )
    CSSColorConst.BURLYWOOD = _RGBColor.to_css(
        222,
        184,
        135,
        255,
    )
    CSSColorConst.BURLYWOOD1 = _RGBColor.to_css(
        255,
        211,
        155,
        255,
    )
    CSSColorConst.BURLYWOOD2 = _RGBColor.to_css(
        238,
        197,
        145,
        255,
    )
    CSSColorConst.BURLYWOOD3 = _RGBColor.to_css(
        205,
        170,
        125,
        255,
    )
    CSSColorConst.BURLYWOOD4 = _RGBColor.to_css(
        139,
        115,
        85,
        255,
    )
    CSSColorConst.CADETBLUE = _RGBColor.to_css(
        95,
        158,
        160,
        255,
    )
    CSSColorConst.CADETBLUE1 = _RGBColor.to_css(
        152,
        245,
        255,
        255,
    )
    CSSColorConst.CADETBLUE2 = _RGBColor.to_css(
        142,
        229,
        238,
        255,
    )
    CSSColorConst.CADETBLUE3 = _RGBColor.to_css(
        122,
        197,
        205,
        255,
    )
    CSSColorConst.CADETBLUE4 = _RGBColor.to_css(
        83,
        134,
        139,
        255,
    )
    CSSColorConst.CHARTREUSE = _RGBColor.to_css(
        127,
        255,
        0,
        255,
    )
    CSSColorConst.CHARTREUSE2 = _RGBColor.to_css(
        118,
        238,
        0,
        255,
    )
    CSSColorConst.CHARTREUSE3 = _RGBColor.to_css(
        102,
        205,
        0,
        255,
    )
    CSSColorConst.CHARTREUSE4 = _RGBColor.to_css(
        69,
        139,
        0,
        255,
    )
    CSSColorConst.CHOCOLATE = _RGBColor.to_css(
        210,
        105,
        30,
        255,
    )
    CSSColorConst.CHOCOLATE1 = _RGBColor.to_css(
        255,
        127,
        36,
        255,
    )
    CSSColorConst.CHOCOLATE2 = _RGBColor.to_css(
        238,
        118,
        33,
        255,
    )
    CSSColorConst.CHOCOLATE3 = _RGBColor.to_css(
        205,
        102,
        29,
        255,
    )
    CSSColorConst.CHOCOLATE4 = _RGBColor.to_css(
        139,
        69,
        19,
        255,
    )
    CSSColorConst.CORAL = _RGBColor.to_css(
        255,
        127,
        80,
        255,
    )
    CSSColorConst.CORAL1 = _RGBColor.to_css(
        255,
        114,
        86,
        255,
    )
    CSSColorConst.CORAL2 = _RGBColor.to_css(
        238,
        106,
        80,
        255,
    )
    CSSColorConst.CORAL3 = _RGBColor.to_css(
        205,
        91,
        69,
        255,
    )
    CSSColorConst.CORAL4 = _RGBColor.to_css(
        139,
        62,
        47,
        255,
    )
    CSSColorConst.CORNFLOWERBLUE = _RGBColor.to_css(
        100,
        149,
        237,
        255,
    )
    CSSColorConst.CORNSILK = _RGBColor.to_css(
        255,
        248,
        220,
        255,
    )
    CSSColorConst.CORNSILK2 = _RGBColor.to_css(
        238,
        232,
        205,
        255,
    )
    CSSColorConst.CORNSILK3 = _RGBColor.to_css(
        205,
        200,
        177,
        255,
    )
    CSSColorConst.CORNSILK4 = _RGBColor.to_css(
        139,
        136,
        120,
        255,
    )
    CSSColorConst.CRIMSON = _RGBColor.to_css(
        220,
        20,
        60,
        255,
    )
    CSSColorConst.CYAN2 = _RGBColor.to_css(
        0,
        238,
        238,
        255,
    )
    CSSColorConst.CYAN3 = _RGBColor.to_css(
        0,
        205,
        205,
        255,
    )
    CSSColorConst.CYAN4 = _RGBColor.to_css(
        0,
        139,
        139,
        255,
    )
    CSSColorConst.DARK_GOLDENROD = _RGBColor.to_css(
        184,
        134,
        11,
        255,
    )
    CSSColorConst.DARK_GOLDENROD1 = _RGBColor.to_css(
        255,
        185,
        15,
        255,
    )
    CSSColorConst.DARK_GOLDENROD2 = _RGBColor.to_css(
        238,
        173,
        14,
        255,
    )
    CSSColorConst.DARK_GOLDENROD3 = _RGBColor.to_css(
        205,
        149,
        12,
        255,
    )
    CSSColorConst.DARK_GOLDENROD4 = _RGBColor.to_css(
        139,
        101,
        8,
        255,
    )
    CSSColorConst.DARK_GRAY = _RGBColor.to_css(
        169,
        169,
        169,
        255,
    )
    CSSColorConst.DARK_GREEN = _RGBColor.to_css(
        0,
        100,
        0,
        255,
    )
    CSSColorConst.DARK_KHAKI = _RGBColor.to_css(
        189,
        183,
        107,
        255,
    )
    CSSColorConst.DARK_MAGENTA = _RGBColor.to_css(
        139,
        0,
        139,
        255,
    )
    CSSColorConst.DARK_OLIVEGREEN = _RGBColor.to_css(
        85,
        107,
        47,
        255,
    )
    CSSColorConst.DARK_OLIVEGREEN1 = _RGBColor.to_css(
        202,
        255,
        112,
        255,
    )
    CSSColorConst.DARK_OLIVEGREEN2 = _RGBColor.to_css(
        188,
        238,
        104,
        255,
    )
    CSSColorConst.DARK_OLIVEGREEN3 = _RGBColor.to_css(
        162,
        205,
        90,
        255,
    )
    CSSColorConst.DARK_OLIVEGREEN4 = _RGBColor.to_css(
        110,
        139,
        61,
        255,
    )
    CSSColorConst.DARK_ORANGE = _RGBColor.to_css(
        255,
        140,
        0,
        255,
    )
    CSSColorConst.DARK_ORANGE1 = _RGBColor.to_css(
        255,
        127,
        0,
        255,
    )
    CSSColorConst.DARK_ORANGE2 = _RGBColor.to_css(
        238,
        118,
        0,
        255,
    )
    CSSColorConst.DARK_ORANGE3 = _RGBColor.to_css(
        205,
        102,
        0,
        255,
    )
    CSSColorConst.DARK_ORANGE4 = _RGBColor.to_css(
        139,
        69,
        0,
        255,
    )
    CSSColorConst.DARK_ORCHID = _RGBColor.to_css(
        153,
        50,
        204,
        255,
    )
    CSSColorConst.DARK_ORCHID1 = _RGBColor.to_css(
        191,
        62,
        255,
        255,
    )
    CSSColorConst.DARK_ORCHID2 = _RGBColor.to_css(
        178,
        58,
        238,
        255,
    )
    CSSColorConst.DARK_ORCHID3 = _RGBColor.to_css(
        154,
        50,
        205,
        255,
    )
    CSSColorConst.DARK_ORCHID4 = _RGBColor.to_css(
        104,
        34,
        139,
        255,
    )
    CSSColorConst.DARK_RED = _RGBColor.to_css(
        139,
        0,
        0,
        255,
    )
    CSSColorConst.DARK_SALMON = _RGBColor.to_css(
        233,
        150,
        122,
        255,
    )
    CSSColorConst.DARK_SEA_GREEN = _RGBColor.to_css(
        143,
        188,
        143,
        255,
    )
    CSSColorConst.DARK_SEA_GREEN1 = _RGBColor.to_css(
        193,
        255,
        193,
        255,
    )
    CSSColorConst.DARK_SEA_GREEN2 = _RGBColor.to_css(
        180,
        238,
        180,
        255,
    )
    CSSColorConst.DARK_SEA_GREEN3 = _RGBColor.to_css(
        155,
        205,
        155,
        255,
    )
    CSSColorConst.DARK_SEA_GREEN4 = _RGBColor.to_css(
        105,
        139,
        105,
        255,
    )
    CSSColorConst.DARK_SLATEBLUE = _RGBColor.to_css(
        72,
        61,
        139,
        255,
    )
    CSSColorConst.DARK_SLATEGRAY = _RGBColor.to_css(
        47,
        79,
        79,
        255,
    )
    CSSColorConst.DARK_SLATEGRAY1 = _RGBColor.to_css(
        151,
        255,
        255,
        255,
    )
    CSSColorConst.DARK_SLATEGRAY2 = _RGBColor.to_css(
        141,
        238,
        238,
        255,
    )
    CSSColorConst.DARK_SLATEGRAY3 = _RGBColor.to_css(
        121,
        205,
        205,
        255,
    )
    CSSColorConst.DARK_SLATEGRAY4 = _RGBColor.to_css(
        82,
        139,
        139,
        255,
    )
    CSSColorConst.DARK_TURQUOISE = _RGBColor.to_css(
        0,
        206,
        209,
        255,
    )
    CSSColorConst.DARK_VIOLET = _RGBColor.to_css(
        148,
        0,
        211,
        255,
    )
    CSSColorConst.DEEP_PINK = _RGBColor.to_css(
        255,
        20,
        147,
        255,
    )
    CSSColorConst.DEEP_PINK2 = _RGBColor.to_css(
        238,
        18,
        137,
        255,
    )
    CSSColorConst.DEEP_PINK3 = _RGBColor.to_css(
        205,
        16,
        118,
        255,
    )
    CSSColorConst.DEEP_PINK4 = _RGBColor.to_css(
        139,
        10,
        80,
        255,
    )
    CSSColorConst.DEEP_SKYBLUE = _RGBColor.to_css(
        0,
        191,
        255,
        255,
    )
    CSSColorConst.DEEP_SKYBLUE2 = _RGBColor.to_css(
        0,
        178,
        238,
        255,
    )
    CSSColorConst.DEEP_SKYBLUE3 = _RGBColor.to_css(
        0,
        154,
        205,
        255,
    )
    CSSColorConst.DEEP_SKYBLUE4 = _RGBColor.to_css(
        0,
        104,
        139,
        255,
    )
    CSSColorConst.DIMGRAY = _RGBColor.to_css(
        105,
        105,
        105,
        255,
    )
    CSSColorConst.DODGERBLUE = _RGBColor.to_css(
        30,
        144,
        255,
        255,
    )
    CSSColorConst.DODGERBLUE2 = _RGBColor.to_css(
        28,
        134,
        238,
        255,
    )
    CSSColorConst.DODGERBLUE3 = _RGBColor.to_css(
        24,
        116,
        205,
        255,
    )
    CSSColorConst.DODGERBLUE4 = _RGBColor.to_css(
        16,
        78,
        139,
        255,
    )
    CSSColorConst.FIRE_BRICK = _RGBColor.to_css(
        178,
        34,
        34,
        255,
    )
    CSSColorConst.FIRE_BRICK1 = _RGBColor.to_css(
        255,
        48,
        48,
        255,
    )
    CSSColorConst.FIRE_BRICK2 = _RGBColor.to_css(
        238,
        44,
        44,
        255,
    )
    CSSColorConst.FIRE_BRICK3 = _RGBColor.to_css(
        205,
        38,
        38,
        255,
    )
    CSSColorConst.FIRE_BRICK4 = _RGBColor.to_css(
        139,
        26,
        26,
        255,
    )
    CSSColorConst.FLORALWHITE = _RGBColor.to_css(
        255,
        250,
        240,
        255,
    )
    CSSColorConst.FORESTGREEN = _RGBColor.to_css(
        34,
        139,
        34,
        255,
    )
    CSSColorConst.FUCHSIA = _RGBColor.to_css(
        255,
        0,
        255,
        255,
    )
    CSSColorConst.GAINSBORO = _RGBColor.to_css(
        220,
        220,
        220,
        255,
    )
    CSSColorConst.GHOSTWHITE = _RGBColor.to_css(
        248,
        248,
        255,
        255,
    )
    CSSColorConst.GOLD = _RGBColor.to_css(
        255,
        215,
        0,
        255,
    )
    CSSColorConst.GOLD2 = _RGBColor.to_css(
        238,
        201,
        0,
        255,
    )
    CSSColorConst.GOLD3 = _RGBColor.to_css(
        205,
        173,
        0,
        255,
    )
    CSSColorConst.GOLD4 = _RGBColor.to_css(
        139,
        117,
        0,
        255,
    )
    CSSColorConst.GOLDENROD = _RGBColor.to_css(
        218,
        165,
        32,
        255,
    )
    CSSColorConst.GOLDENROD1 = _RGBColor.to_css(
        255,
        193,
        37,
        255,
    )
    CSSColorConst.GOLDENROD2 = _RGBColor.to_css(
        238,
        180,
        34,
        255,
    )
    CSSColorConst.GOLDENROD3 = _RGBColor.to_css(
        205,
        155,
        29,
        255,
    )
    CSSColorConst.GOLDENROD4 = _RGBColor.to_css(
        139,
        105,
        20,
        255,
    )
    CSSColorConst.GRAY = _RGBColor.to_css(
        190,
        190,
        190,
        255,
    )
    CSSColorConst.GRAY1 = _RGBColor.to_css(
        3,
        3,
        3,
        255,
    )
    CSSColorConst.GRAY10 = _RGBColor.to_css(
        26,
        26,
        26,
        255,
    )
    CSSColorConst.GRAY100 = _RGBColor.to_css(
        255,
        255,
        255,
        255,
    )
    CSSColorConst.GRAY11 = _RGBColor.to_css(
        28,
        28,
        28,
        255,
    )
    CSSColorConst.GRAY12 = _RGBColor.to_css(
        31,
        31,
        31,
        255,
    )
    CSSColorConst.GRAY13 = _RGBColor.to_css(
        33,
        33,
        33,
        255,
    )
    CSSColorConst.GRAY14 = _RGBColor.to_css(
        36,
        36,
        36,
        255,
    )
    CSSColorConst.GRAY15 = _RGBColor.to_css(
        38,
        38,
        38,
        255,
    )
    CSSColorConst.GRAY16 = _RGBColor.to_css(
        41,
        41,
        41,
        255,
    )
    CSSColorConst.GRAY17 = _RGBColor.to_css(
        43,
        43,
        43,
        255,
    )
    CSSColorConst.GRAY18 = _RGBColor.to_css(
        46,
        46,
        46,
        255,
    )
    CSSColorConst.GRAY19 = _RGBColor.to_css(
        48,
        48,
        48,
        255,
    )
    CSSColorConst.GRAY2 = _RGBColor.to_css(
        5,
        5,
        5,
        255,
    )
    CSSColorConst.GRAY20 = _RGBColor.to_css(
        51,
        51,
        51,
        255,
    )
    CSSColorConst.GRAY21 = _RGBColor.to_css(
        54,
        54,
        54,
        255,
    )
    CSSColorConst.GRAY22 = _RGBColor.to_css(
        56,
        56,
        56,
        255,
    )
    CSSColorConst.GRAY23 = _RGBColor.to_css(
        59,
        59,
        59,
        255,
    )
    CSSColorConst.GRAY24 = _RGBColor.to_css(
        61,
        61,
        61,
        255,
    )
    CSSColorConst.GRAY25 = _RGBColor.to_css(
        64,
        64,
        64,
        255,
    )
    CSSColorConst.GRAY26 = _RGBColor.to_css(
        66,
        66,
        66,
        255,
    )
    CSSColorConst.GRAY27 = _RGBColor.to_css(
        69,
        69,
        69,
        255,
    )
    CSSColorConst.GRAY28 = _RGBColor.to_css(
        71,
        71,
        71,
        255,
    )
    CSSColorConst.GRAY29 = _RGBColor.to_css(
        74,
        74,
        74,
        255,
    )
    CSSColorConst.GRAY3 = _RGBColor.to_css(
        8,
        8,
        8,
        255,
    )
    CSSColorConst.GRAY30 = _RGBColor.to_css(
        77,
        77,
        77,
        255,
    )
    CSSColorConst.GRAY31 = _RGBColor.to_css(
        79,
        79,
        79,
        255,
    )
    CSSColorConst.GRAY32 = _RGBColor.to_css(
        82,
        82,
        82,
        255,
    )
    CSSColorConst.GRAY33 = _RGBColor.to_css(
        84,
        84,
        84,
        255,
    )
    CSSColorConst.GRAY34 = _RGBColor.to_css(
        87,
        87,
        87,
        255,
    )
    CSSColorConst.GRAY35 = _RGBColor.to_css(
        89,
        89,
        89,
        255,
    )
    CSSColorConst.GRAY36 = _RGBColor.to_css(
        92,
        92,
        92,
        255,
    )
    CSSColorConst.GRAY37 = _RGBColor.to_css(
        94,
        94,
        94,
        255,
    )
    CSSColorConst.GRAY38 = _RGBColor.to_css(
        97,
        97,
        97,
        255,
    )
    CSSColorConst.GRAY39 = _RGBColor.to_css(
        99,
        99,
        99,
        255,
    )
    CSSColorConst.GRAY4 = _RGBColor.to_css(
        10,
        10,
        10,
        255,
    )
    CSSColorConst.GRAY40 = _RGBColor.to_css(
        102,
        102,
        102,
        255,
    )
    CSSColorConst.GRAY42 = _RGBColor.to_css(
        107,
        107,
        107,
        255,
    )
    CSSColorConst.GRAY43 = _RGBColor.to_css(
        110,
        110,
        110,
        255,
    )
    CSSColorConst.GRAY44 = _RGBColor.to_css(
        112,
        112,
        112,
        255,
    )
    CSSColorConst.GRAY45 = _RGBColor.to_css(
        115,
        115,
        115,
        255,
    )
    CSSColorConst.GRAY46 = _RGBColor.to_css(
        117,
        117,
        117,
        255,
    )
    CSSColorConst.GRAY47 = _RGBColor.to_css(
        120,
        120,
        120,
        255,
    )
    CSSColorConst.GRAY48 = _RGBColor.to_css(
        122,
        122,
        122,
        255,
    )
    CSSColorConst.GRAY49 = _RGBColor.to_css(
        125,
        125,
        125,
        255,
    )
    CSSColorConst.GRAY5 = _RGBColor.to_css(
        13,
        13,
        13,
        255,
    )
    CSSColorConst.GRAY50 = _RGBColor.to_css(
        127,
        127,
        127,
        255,
    )
    CSSColorConst.GRAY51 = _RGBColor.to_css(
        130,
        130,
        130,
        255,
    )
    CSSColorConst.GRAY52 = _RGBColor.to_css(
        133,
        133,
        133,
        255,
    )
    CSSColorConst.GRAY53 = _RGBColor.to_css(
        135,
        135,
        135,
        255,
    )
    CSSColorConst.GRAY54 = _RGBColor.to_css(
        138,
        138,
        138,
        255,
    )
    CSSColorConst.GRAY55 = _RGBColor.to_css(
        140,
        140,
        140,
        255,
    )
    CSSColorConst.GRAY56 = _RGBColor.to_css(
        143,
        143,
        143,
        255,
    )
    CSSColorConst.GRAY57 = _RGBColor.to_css(
        145,
        145,
        145,
        255,
    )
    CSSColorConst.GRAY58 = _RGBColor.to_css(
        148,
        148,
        148,
        255,
    )
    CSSColorConst.GRAY59 = _RGBColor.to_css(
        150,
        150,
        150,
        255,
    )
    CSSColorConst.GRAY6 = _RGBColor.to_css(
        15,
        15,
        15,
        255,
    )
    CSSColorConst.GRAY60 = _RGBColor.to_css(
        153,
        153,
        153,
        255,
    )
    CSSColorConst.GRAY61 = _RGBColor.to_css(
        156,
        156,
        156,
        255,
    )
    CSSColorConst.GRAY62 = _RGBColor.to_css(
        158,
        158,
        158,
        255,
    )
    CSSColorConst.GRAY63 = _RGBColor.to_css(
        161,
        161,
        161,
        255,
    )
    CSSColorConst.GRAY64 = _RGBColor.to_css(
        163,
        163,
        163,
        255,
    )
    CSSColorConst.GRAY65 = _RGBColor.to_css(
        166,
        166,
        166,
        255,
    )
    CSSColorConst.GRAY66 = _RGBColor.to_css(
        168,
        168,
        168,
        255,
    )
    CSSColorConst.GRAY67 = _RGBColor.to_css(
        171,
        171,
        171,
        255,
    )
    CSSColorConst.GRAY68 = _RGBColor.to_css(
        173,
        173,
        173,
        255,
    )
    CSSColorConst.GRAY69 = _RGBColor.to_css(
        176,
        176,
        176,
        255,
    )
    CSSColorConst.GRAY7 = _RGBColor.to_css(
        18,
        18,
        18,
        255,
    )
    CSSColorConst.GRAY70 = _RGBColor.to_css(
        179,
        179,
        179,
        255,
    )
    CSSColorConst.GRAY71 = _RGBColor.to_css(
        181,
        181,
        181,
        255,
    )
    CSSColorConst.GRAY72 = _RGBColor.to_css(
        184,
        184,
        184,
        255,
    )
    CSSColorConst.GRAY73 = _RGBColor.to_css(
        186,
        186,
        186,
        255,
    )
    CSSColorConst.GRAY74 = _RGBColor.to_css(
        189,
        189,
        189,
        255,
    )
    CSSColorConst.GRAY75 = _RGBColor.to_css(
        191,
        191,
        191,
        255,
    )
    CSSColorConst.GRAY76 = _RGBColor.to_css(
        194,
        194,
        194,
        255,
    )
    CSSColorConst.GRAY77 = _RGBColor.to_css(
        196,
        196,
        196,
        255,
    )
    CSSColorConst.GRAY78 = _RGBColor.to_css(
        199,
        199,
        199,
        255,
    )
    CSSColorConst.GRAY79 = _RGBColor.to_css(
        201,
        201,
        201,
        255,
    )
    CSSColorConst.GRAY8 = _RGBColor.to_css(
        20,
        20,
        20,
        255,
    )
    CSSColorConst.GRAY80 = _RGBColor.to_css(
        204,
        204,
        204,
        255,
    )
    CSSColorConst.GRAY81 = _RGBColor.to_css(
        207,
        207,
        207,
        255,
    )
    CSSColorConst.GRAY82 = _RGBColor.to_css(
        209,
        209,
        209,
        255,
    )
    CSSColorConst.GRAY83 = _RGBColor.to_css(
        212,
        212,
        212,
        255,
    )
    CSSColorConst.GRAY84 = _RGBColor.to_css(
        214,
        214,
        214,
        255,
    )
    CSSColorConst.GRAY85 = _RGBColor.to_css(
        217,
        217,
        217,
        255,
    )
    CSSColorConst.GRAY86 = _RGBColor.to_css(
        219,
        219,
        219,
        255,
    )
    CSSColorConst.GRAY87 = _RGBColor.to_css(
        222,
        222,
        222,
        255,
    )
    CSSColorConst.GRAY88 = _RGBColor.to_css(
        224,
        224,
        224,
        255,
    )
    CSSColorConst.GRAY89 = _RGBColor.to_css(
        227,
        227,
        227,
        255,
    )
    CSSColorConst.GRAY9 = _RGBColor.to_css(
        23,
        23,
        23,
        255,
    )
    CSSColorConst.GRAY90 = _RGBColor.to_css(
        229,
        229,
        229,
        255,
    )
    CSSColorConst.GRAY91 = _RGBColor.to_css(
        232,
        232,
        232,
        255,
    )
    CSSColorConst.GRAY92 = _RGBColor.to_css(
        235,
        235,
        235,
        255,
    )
    CSSColorConst.GRAY93 = _RGBColor.to_css(
        237,
        237,
        237,
        255,
    )
    CSSColorConst.GRAY94 = _RGBColor.to_css(
        240,
        240,
        240,
        255,
    )
    CSSColorConst.GRAY95 = _RGBColor.to_css(
        242,
        242,
        242,
        255,
    )
    CSSColorConst.GRAY96 = _RGBColor.to_css(
        245,
        245,
        245,
        255,
    )
    CSSColorConst.GRAY97 = _RGBColor.to_css(
        247,
        247,
        247,
        255,
    )
    CSSColorConst.GRAY98 = _RGBColor.to_css(
        250,
        250,
        250,
        255,
    )
    CSSColorConst.GRAY99 = _RGBColor.to_css(
        252,
        252,
        252,
        255,
    )
    CSSColorConst.GREEN = _RGBColor.to_css(
        0,
        255,
        0,
        255,
    )
    CSSColorConst.GREEN2 = _RGBColor.to_css(
        0,
        238,
        0,
        255,
    )
    CSSColorConst.GREEN3 = _RGBColor.to_css(
        0,
        205,
        0,
        255,
    )
    CSSColorConst.GREEN4 = _RGBColor.to_css(
        0,
        139,
        0,
        255,
    )
    CSSColorConst.GREENYELLOW = _RGBColor.to_css(
        173,
        255,
        47,
        255,
    )
    CSSColorConst.HONEYDEW = _RGBColor.to_css(
        240,
        255,
        240,
        255,
    )
    CSSColorConst.HONEYDEW2 = _RGBColor.to_css(
        224,
        238,
        224,
        255,
    )
    CSSColorConst.HONEYDEW3 = _RGBColor.to_css(
        193,
        205,
        193,
        255,
    )
    CSSColorConst.HONEYDEW4 = _RGBColor.to_css(
        131,
        139,
        131,
        255,
    )
    CSSColorConst.HOT_PINK = _RGBColor.to_css(
        255,
        105,
        180,
        255,
    )
    CSSColorConst.HOT_PINK1 = _RGBColor.to_css(
        255,
        110,
        180,
        255,
    )
    CSSColorConst.HOT_PINK2 = _RGBColor.to_css(
        238,
        106,
        167,
        255,
    )
    CSSColorConst.HOT_PINK3 = _RGBColor.to_css(
        205,
        96,
        144,
        255,
    )
    CSSColorConst.HOT_PINK4 = _RGBColor.to_css(
        139,
        58,
        98,
        255,
    )
    CSSColorConst.INDIANRED = _RGBColor.to_css(
        205,
        92,
        92,
        255,
    )
    CSSColorConst.INDIANRED1 = _RGBColor.to_css(
        255,
        106,
        106,
        255,
    )
    CSSColorConst.INDIANRED2 = _RGBColor.to_css(
        238,
        99,
        99,
        255,
    )
    CSSColorConst.INDIANRED3 = _RGBColor.to_css(
        205,
        85,
        85,
        255,
    )
    CSSColorConst.INDIANRED4 = _RGBColor.to_css(
        139,
        58,
        58,
        255,
    )
    CSSColorConst.INDIGO = _RGBColor.to_css(
        75,
        0,
        130,
        255,
    )
    CSSColorConst.IVORY = _RGBColor.to_css(
        255,
        255,
        240,
        255,
    )
    CSSColorConst.IVORY2 = _RGBColor.to_css(
        238,
        238,
        224,
        255,
    )
    CSSColorConst.IVORY3 = _RGBColor.to_css(
        205,
        205,
        193,
        255,
    )
    CSSColorConst.IVORY4 = _RGBColor.to_css(
        139,
        139,
        131,
        255,
    )
    CSSColorConst.KHAKI = _RGBColor.to_css(
        240,
        230,
        140,
        255,
    )
    CSSColorConst.KHAKI1 = _RGBColor.to_css(
        255,
        246,
        143,
        255,
    )
    CSSColorConst.KHAKI2 = _RGBColor.to_css(
        238,
        230,
        133,
        255,
    )
    CSSColorConst.KHAKI3 = _RGBColor.to_css(
        205,
        198,
        115,
        255,
    )
    CSSColorConst.KHAKI4 = _RGBColor.to_css(
        139,
        134,
        78,
        255,
    )
    CSSColorConst.LAVENDER = _RGBColor.to_css(
        230,
        230,
        250,
        255,
    )
    CSSColorConst.LAVENDERBLUSH = _RGBColor.to_css(
        255,
        240,
        245,
        255,
    )
    CSSColorConst.LAVENDERBLUSH2 = _RGBColor.to_css(
        238,
        224,
        229,
        255,
    )
    CSSColorConst.LAVENDERBLUSH3 = _RGBColor.to_css(
        205,
        193,
        197,
        255,
    )
    CSSColorConst.LAVENDERBLUSH4 = _RGBColor.to_css(
        139,
        131,
        134,
        255,
    )
    CSSColorConst.LAWNGREEN = _RGBColor.to_css(
        124,
        252,
        0,
        255,
    )
    CSSColorConst.LEMONCHIFFON = _RGBColor.to_css(
        255,
        250,
        205,
        255,
    )
    CSSColorConst.LEMONCHIFFON2 = _RGBColor.to_css(
        238,
        233,
        191,
        255,
    )
    CSSColorConst.LEMONCHIFFON3 = _RGBColor.to_css(
        205,
        201,
        165,
        255,
    )
    CSSColorConst.LEMONCHIFFON4 = _RGBColor.to_css(
        139,
        137,
        112,
        255,
    )
    CSSColorConst.LIGHT_BLUE = _RGBColor.to_css(
        173,
        216,
        230,
        255,
    )
    CSSColorConst.LIGHT_BLUE1 = _RGBColor.to_css(
        191,
        239,
        255,
        255,
    )
    CSSColorConst.LIGHT_BLUE2 = _RGBColor.to_css(
        178,
        223,
        238,
        255,
    )
    CSSColorConst.LIGHT_BLUE3 = _RGBColor.to_css(
        154,
        192,
        205,
        255,
    )
    CSSColorConst.LIGHT_BLUE4 = _RGBColor.to_css(
        104,
        131,
        139,
        255,
    )
    CSSColorConst.LIGHT_CORAL = _RGBColor.to_css(
        240,
        128,
        128,
        255,
    )
    CSSColorConst.LIGHT_CYAN = _RGBColor.to_css(
        224,
        255,
        255,
        255,
    )
    CSSColorConst.LIGHT_CYAN2 = _RGBColor.to_css(
        209,
        238,
        238,
        255,
    )
    CSSColorConst.LIGHT_CYAN3 = _RGBColor.to_css(
        180,
        205,
        205,
        255,
    )
    CSSColorConst.LIGHT_CYAN4 = _RGBColor.to_css(
        122,
        139,
        139,
        255,
    )
    CSSColorConst.LIGHT_GOLDENROD = _RGBColor.to_css(
        238,
        221,
        130,
        255,
    )
    CSSColorConst.LIGHT_GOLDENROD1 = _RGBColor.to_css(
        255,
        236,
        139,
        255,
    )
    CSSColorConst.LIGHT_GOLDENROD2 = _RGBColor.to_css(
        238,
        220,
        130,
        255,
    )
    CSSColorConst.LIGHT_GOLDENROD3 = _RGBColor.to_css(
        205,
        190,
        112,
        255,
    )
    CSSColorConst.LIGHT_GOLDENROD4 = _RGBColor.to_css(
        139,
        129,
        76,
        255,
    )
    CSSColorConst.LIGHT_GOLDENRODYELLOW = _RGBColor.to_css(
        250,
        250,
        210,
        255,
    )
    CSSColorConst.LIGHT_GRAY = _RGBColor.to_css(
        211,
        211,
        211,
        255,
    )
    CSSColorConst.LIGHT_GREEN = _RGBColor.to_css(
        144,
        238,
        144,
        255,
    )
    CSSColorConst.LIGHT_PINK = _RGBColor.to_css(
        255,
        182,
        193,
        255,
    )
    CSSColorConst.LIGHT_PINK1 = _RGBColor.to_css(
        255,
        174,
        185,
        255,
    )
    CSSColorConst.LIGHT_PINK2 = _RGBColor.to_css(
        238,
        162,
        173,
        255,
    )
    CSSColorConst.LIGHT_PINK3 = _RGBColor.to_css(
        205,
        140,
        149,
        255,
    )
    CSSColorConst.LIGHT_PINK4 = _RGBColor.to_css(
        139,
        95,
        101,
        255,
    )
    CSSColorConst.LIGHT_SALMON = _RGBColor.to_css(
        255,
        160,
        122,
        255,
    )
    CSSColorConst.LIGHT_SALMON2 = _RGBColor.to_css(
        238,
        149,
        114,
        255,
    )
    CSSColorConst.LIGHT_SALMON3 = _RGBColor.to_css(
        205,
        129,
        98,
        255,
    )
    CSSColorConst.LIGHT_SALMON4 = _RGBColor.to_css(
        139,
        87,
        66,
        255,
    )
    CSSColorConst.LIGHT_SEA_GREEN = _RGBColor.to_css(
        32,
        178,
        170,
        255,
    )
    CSSColorConst.LIGHT_SKYBLUE = _RGBColor.to_css(
        135,
        206,
        250,
        255,
    )
    CSSColorConst.LIGHT_SKYBLUE1 = _RGBColor.to_css(
        176,
        226,
        255,
        255,
    )
    CSSColorConst.LIGHT_SKYBLUE2 = _RGBColor.to_css(
        164,
        211,
        238,
        255,
    )
    CSSColorConst.LIGHT_SKYBLUE3 = _RGBColor.to_css(
        141,
        182,
        205,
        255,
    )
    CSSColorConst.LIGHT_SKYBLUE4 = _RGBColor.to_css(
        96,
        123,
        139,
        255,
    )
    CSSColorConst.LIGHT_SLATEBLUE = _RGBColor.to_css(
        132,
        112,
        255,
        255,
    )
    CSSColorConst.LIGHT_SLATEGRAY = _RGBColor.to_css(
        119,
        136,
        153,
        255,
    )
    CSSColorConst.LIGHT_STEELBLUE = _RGBColor.to_css(
        176,
        196,
        222,
        255,
    )
    CSSColorConst.LIGHT_STEELBLUE1 = _RGBColor.to_css(
        202,
        225,
        255,
        255,
    )
    CSSColorConst.LIGHT_STEELBLUE2 = _RGBColor.to_css(
        188,
        210,
        238,
        255,
    )
    CSSColorConst.LIGHT_STEELBLUE3 = _RGBColor.to_css(
        162,
        181,
        205,
        255,
    )
    CSSColorConst.LIGHT_STEELBLUE4 = _RGBColor.to_css(
        110,
        123,
        139,
        255,
    )
    CSSColorConst.LIGHT_YELLOW = _RGBColor.to_css(
        255,
        255,
        224,
        255,
    )
    CSSColorConst.LIGHT_YELLOW2 = _RGBColor.to_css(
        238,
        238,
        209,
        255,
    )
    CSSColorConst.LIGHT_YELLOW3 = _RGBColor.to_css(
        205,
        205,
        180,
        255,
    )
    CSSColorConst.LIGHT_YELLOW4 = _RGBColor.to_css(
        139,
        139,
        122,
        255,
    )
    CSSColorConst.LIME_GREEN = _RGBColor.to_css(
        50,
        205,
        50,
        255,
    )
    CSSColorConst.LINEN = _RGBColor.to_css(
        250,
        240,
        230,
        255,
    )
    CSSColorConst.MAGENTA2 = _RGBColor.to_css(
        238,
        0,
        238,
        255,
    )
    CSSColorConst.MAGENTA3 = _RGBColor.to_css(
        205,
        0,
        205,
        255,
    )
    CSSColorConst.MAROON = _RGBColor.to_css(
        176,
        48,
        96,
        255,
    )
    CSSColorConst.MAROON1 = _RGBColor.to_css(
        255,
        52,
        179,
        255,
    )
    CSSColorConst.MAROON2 = _RGBColor.to_css(
        238,
        48,
        167,
        255,
    )
    CSSColorConst.MAROON3 = _RGBColor.to_css(
        205,
        41,
        144,
        255,
    )
    CSSColorConst.MAROON4 = _RGBColor.to_css(
        139,
        28,
        98,
        255,
    )
    CSSColorConst.MEDIUM_ORCHID = _RGBColor.to_css(
        186,
        85,
        211,
        255,
    )
    CSSColorConst.MEDIUM_ORCHID1 = _RGBColor.to_css(
        224,
        102,
        255,
        255,
    )
    CSSColorConst.MEDIUM_ORCHID2 = _RGBColor.to_css(
        209,
        95,
        238,
        255,
    )
    CSSColorConst.MEDIUM_ORCHID3 = _RGBColor.to_css(
        180,
        82,
        205,
        255,
    )
    CSSColorConst.MEDIUM_ORCHID4 = _RGBColor.to_css(
        122,
        55,
        139,
        255,
    )
    CSSColorConst.MEDIUM_PURPLE = _RGBColor.to_css(
        147,
        112,
        219,
        255,
    )
    CSSColorConst.MEDIUM_PURPLE1 = _RGBColor.to_css(
        171,
        130,
        255,
        255,
    )
    CSSColorConst.MEDIUM_PURPLE2 = _RGBColor.to_css(
        159,
        121,
        238,
        255,
    )
    CSSColorConst.MEDIUM_PURPLE3 = _RGBColor.to_css(
        137,
        104,
        205,
        255,
    )
    CSSColorConst.MEDIUM_PURPLE4 = _RGBColor.to_css(
        93,
        71,
        139,
        255,
    )
    CSSColorConst.MEDIUM_SEA_GREEN = _RGBColor.to_css(
        60,
        179,
        113,
        255,
    )
    CSSColorConst.MEDIUM_SLATEBLUE = _RGBColor.to_css(
        123,
        104,
        238,
        255,
    )
    CSSColorConst.MEDIUM_SPRINGGREEN = _RGBColor.to_css(
        0,
        250,
        154,
        255,
    )
    CSSColorConst.MEDIUM_TURQUOISE = _RGBColor.to_css(
        72,
        209,
        204,
        255,
    )
    CSSColorConst.MEDIUM_VIOLETRED = _RGBColor.to_css(
        199,
        21,
        133,
        255,
    )
    CSSColorConst.MIDNIGHTBLUE = _RGBColor.to_css(
        25,
        25,
        112,
        255,
    )
    CSSColorConst.MINTCREAM = _RGBColor.to_css(
        245,
        255,
        250,
        255,
    )
    CSSColorConst.MISTYROSE = _RGBColor.to_css(
        255,
        228,
        225,
        255,
    )
    CSSColorConst.MISTYROSE2 = _RGBColor.to_css(
        238,
        213,
        210,
        255,
    )
    CSSColorConst.MISTYROSE3 = _RGBColor.to_css(
        205,
        183,
        181,
        255,
    )
    CSSColorConst.MISTYROSE4 = _RGBColor.to_css(
        139,
        125,
        123,
        255,
    )
    CSSColorConst.MOCCASIN = _RGBColor.to_css(
        255,
        228,
        181,
        255,
    )
    CSSColorConst.NAVAJOWHITE = _RGBColor.to_css(
        255,
        222,
        173,
        255,
    )
    CSSColorConst.NAVAJOWHITE2 = _RGBColor.to_css(
        238,
        207,
        161,
        255,
    )
    CSSColorConst.NAVAJOWHITE3 = _RGBColor.to_css(
        205,
        179,
        139,
        255,
    )
    CSSColorConst.NAVAJOWHITE4 = _RGBColor.to_css(
        139,
        121,
        94,
        255,
    )
    CSSColorConst.NAVY = _RGBColor.to_css(
        0,
        0,
        128,
        255,
    )
    CSSColorConst.OLDLACE = _RGBColor.to_css(
        253,
        245,
        230,
        255,
    )
    CSSColorConst.OLIVE = _RGBColor.to_css(
        128,
        128,
        0,
        255,
    )
    CSSColorConst.OLIVEDRAB = _RGBColor.to_css(
        107,
        142,
        35,
        255,
    )
    CSSColorConst.OLIVEDRAB1 = _RGBColor.to_css(
        192,
        255,
        62,
        255,
    )
    CSSColorConst.OLIVEDRAB2 = _RGBColor.to_css(
        179,
        238,
        58,
        255,
    )
    CSSColorConst.OLIVEDRAB3 = _RGBColor.to_css(
        154,
        205,
        50,
        255,
    )
    CSSColorConst.OLIVEDRAB4 = _RGBColor.to_css(
        105,
        139,
        34,
        255,
    )
    CSSColorConst.ORANGE = _RGBColor.to_css(
        255,
        165,
        0,
        255,
    )
    CSSColorConst.ORANGE2 = _RGBColor.to_css(
        238,
        154,
        0,
        255,
    )
    CSSColorConst.ORANGE3 = _RGBColor.to_css(
        205,
        133,
        0,
        255,
    )
    CSSColorConst.ORANGE4 = _RGBColor.to_css(
        139,
        90,
        0,
        255,
    )
    CSSColorConst.ORANGERED = _RGBColor.to_css(
        255,
        69,
        0,
        255,
    )
    CSSColorConst.ORANGERED2 = _RGBColor.to_css(
        238,
        64,
        0,
        255,
    )
    CSSColorConst.ORANGERED3 = _RGBColor.to_css(
        205,
        55,
        0,
        255,
    )
    CSSColorConst.ORANGERED4 = _RGBColor.to_css(
        139,
        37,
        0,
        255,
    )
    CSSColorConst.ORCHID = _RGBColor.to_css(
        218,
        112,
        214,
        255,
    )
    CSSColorConst.ORCHID1 = _RGBColor.to_css(
        255,
        131,
        250,
        255,
    )
    CSSColorConst.ORCHID2 = _RGBColor.to_css(
        238,
        122,
        233,
        255,
    )
    CSSColorConst.ORCHID3 = _RGBColor.to_css(
        205,
        105,
        201,
        255,
    )
    CSSColorConst.ORCHID4 = _RGBColor.to_css(
        139,
        71,
        137,
        255,
    )
    CSSColorConst.PALE_GOLDENROD = _RGBColor.to_css(
        238,
        232,
        170,
        255,
    )
    CSSColorConst.PALE_GREEN = _RGBColor.to_css(
        152,
        251,
        152,
        255,
    )
    CSSColorConst.PALE_GREEN1 = _RGBColor.to_css(
        154,
        255,
        154,
        255,
    )
    CSSColorConst.PALE_GREEN3 = _RGBColor.to_css(
        124,
        205,
        124,
        255,
    )
    CSSColorConst.PALE_GREEN4 = _RGBColor.to_css(
        84,
        139,
        84,
        255,
    )
    CSSColorConst.PALE_TURQUOISE = _RGBColor.to_css(
        175,
        238,
        238,
        255,
    )
    CSSColorConst.PALE_TURQUOISE1 = _RGBColor.to_css(
        187,
        255,
        255,
        255,
    )
    CSSColorConst.PALE_TURQUOISE2 = _RGBColor.to_css(
        174,
        238,
        238,
        255,
    )
    CSSColorConst.PALE_TURQUOISE3 = _RGBColor.to_css(
        150,
        205,
        205,
        255,
    )
    CSSColorConst.PALE_TURQUOISE4 = _RGBColor.to_css(
        102,
        139,
        139,
        255,
    )
    CSSColorConst.PALE_VIOLETRED = _RGBColor.to_css(
        219,
        112,
        147,
        255,
    )
    CSSColorConst.PALE_VIOLETRED1 = _RGBColor.to_css(
        255,
        130,
        171,
        255,
    )
    CSSColorConst.PALE_VIOLETRED2 = _RGBColor.to_css(
        238,
        121,
        159,
        255,
    )
    CSSColorConst.PALE_VIOLETRED3 = _RGBColor.to_css(
        205,
        104,
        137,
        255,
    )
    CSSColorConst.PALE_VIOLETRED4 = _RGBColor.to_css(
        139,
        71,
        93,
        255,
    )
    CSSColorConst.PAPAYAWHIP = _RGBColor.to_css(
        255,
        239,
        213,
        255,
    )
    CSSColorConst.PEACHPUFF = _RGBColor.to_css(
        255,
        218,
        185,
        255,
    )
    CSSColorConst.PEACHPUFF2 = _RGBColor.to_css(
        238,
        203,
        173,
        255,
    )
    CSSColorConst.PEACHPUFF3 = _RGBColor.to_css(
        205,
        175,
        149,
        255,
    )
    CSSColorConst.PEACHPUFF4 = _RGBColor.to_css(
        139,
        119,
        101,
        255,
    )
    CSSColorConst.PERU = _RGBColor.to_css(
        205,
        133,
        63,
        255,
    )
    CSSColorConst.PINK = _RGBColor.to_css(
        255,
        192,
        203,
        255,
    )
    CSSColorConst.PINK1 = _RGBColor.to_css(
        255,
        181,
        197,
        255,
    )
    CSSColorConst.PINK2 = _RGBColor.to_css(
        238,
        169,
        184,
        255,
    )
    CSSColorConst.PINK3 = _RGBColor.to_css(
        205,
        145,
        158,
        255,
    )
    CSSColorConst.PINK4 = _RGBColor.to_css(
        139,
        99,
        108,
        255,
    )
    CSSColorConst.PLUM = _RGBColor.to_css(
        221,
        160,
        221,
        255,
    )
    CSSColorConst.PLUM1 = _RGBColor.to_css(
        255,
        187,
        255,
        255,
    )
    CSSColorConst.PLUM2 = _RGBColor.to_css(
        238,
        174,
        238,
        255,
    )
    CSSColorConst.PLUM3 = _RGBColor.to_css(
        205,
        150,
        205,
        255,
    )
    CSSColorConst.PLUM4 = _RGBColor.to_css(
        139,
        102,
        139,
        255,
    )
    CSSColorConst.POWDERBLUE = _RGBColor.to_css(
        176,
        224,
        230,
        255,
    )
    CSSColorConst.PURPLE = _RGBColor.to_css(
        160,
        32,
        240,
        255,
    )
    CSSColorConst.PURPLE1 = _RGBColor.to_css(
        155,
        48,
        255,
        255,
    )
    CSSColorConst.PURPLE2 = _RGBColor.to_css(
        145,
        44,
        238,
        255,
    )
    CSSColorConst.PURPLE3 = _RGBColor.to_css(
        125,
        38,
        205,
        255,
    )
    CSSColorConst.PURPLE4 = _RGBColor.to_css(
        85,
        26,
        139,
        255,
    )
    CSSColorConst.RED = _RGBColor.to_css(
        255,
        0,
        0,
        255,
    )
    CSSColorConst.RED2 = _RGBColor.to_css(
        238,
        0,
        0,
        255,
    )
    CSSColorConst.RED3 = _RGBColor.to_css(
        205,
        0,
        0,
        255,
    )
    CSSColorConst.ROSYBROWN = _RGBColor.to_css(
        188,
        143,
        143,
        255,
    )
    CSSColorConst.ROSYBROWN1 = _RGBColor.to_css(
        255,
        193,
        193,
        255,
    )
    CSSColorConst.ROSYBROWN2 = _RGBColor.to_css(
        238,
        180,
        180,
        255,
    )
    CSSColorConst.ROSYBROWN3 = _RGBColor.to_css(
        205,
        155,
        155,
        255,
    )
    CSSColorConst.ROSYBROWN4 = _RGBColor.to_css(
        139,
        105,
        105,
        255,
    )
    CSSColorConst.ROYALBLUE = _RGBColor.to_css(
        65,
        105,
        225,
        255,
    )
    CSSColorConst.ROYALBLUE1 = _RGBColor.to_css(
        72,
        118,
        255,
        255,
    )
    CSSColorConst.ROYALBLUE2 = _RGBColor.to_css(
        67,
        110,
        238,
        255,
    )
    CSSColorConst.ROYALBLUE3 = _RGBColor.to_css(
        58,
        95,
        205,
        255,
    )
    CSSColorConst.ROYALBLUE4 = _RGBColor.to_css(
        39,
        64,
        139,
        255,
    )
    CSSColorConst.SALMON = _RGBColor.to_css(
        250,
        128,
        114,
        255,
    )
    CSSColorConst.SALMON1 = _RGBColor.to_css(
        255,
        140,
        105,
        255,
    )
    CSSColorConst.SALMON2 = _RGBColor.to_css(
        238,
        130,
        98,
        255,
    )
    CSSColorConst.SALMON3 = _RGBColor.to_css(
        205,
        112,
        84,
        255,
    )
    CSSColorConst.SALMON4 = _RGBColor.to_css(
        139,
        76,
        57,
        255,
    )
    CSSColorConst.SANDYBROWN = _RGBColor.to_css(
        244,
        164,
        96,
        255,
    )
    CSSColorConst.SEA_GREEN = _RGBColor.to_css(
        46,
        139,
        87,
        255,
    )
    CSSColorConst.SEA_GREEN1 = _RGBColor.to_css(
        84,
        255,
        159,
        255,
    )
    CSSColorConst.SEA_GREEN2 = _RGBColor.to_css(
        78,
        238,
        148,
        255,
    )
    CSSColorConst.SEA_GREEN3 = _RGBColor.to_css(
        67,
        205,
        128,
        255,
    )
    CSSColorConst.SEA_SHELL = _RGBColor.to_css(
        255,
        245,
        238,
        255,
    )
    CSSColorConst.SEA_SHELL2 = _RGBColor.to_css(
        238,
        229,
        222,
        255,
    )
    CSSColorConst.SEA_SHELL3 = _RGBColor.to_css(
        205,
        197,
        191,
        255,
    )
    CSSColorConst.SEA_SHELL4 = _RGBColor.to_css(
        139,
        134,
        130,
        255,
    )
    CSSColorConst.SIENNA = _RGBColor.to_css(
        160,
        82,
        45,
        255,
    )
    CSSColorConst.SIENNA1 = _RGBColor.to_css(
        255,
        130,
        71,
        255,
    )
    CSSColorConst.SIENNA2 = _RGBColor.to_css(
        238,
        121,
        66,
        255,
    )
    CSSColorConst.SIENNA3 = _RGBColor.to_css(
        205,
        104,
        57,
        255,
    )
    CSSColorConst.SIENNA4 = _RGBColor.to_css(
        139,
        71,
        38,
        255,
    )
    CSSColorConst.SILVER = _RGBColor.to_css(
        192,
        192,
        192,
        255,
    )
    CSSColorConst.SKYBLUE = _RGBColor.to_css(
        135,
        206,
        235,
        255,
    )
    CSSColorConst.SKYBLUE1 = _RGBColor.to_css(
        135,
        206,
        255,
        255,
    )
    CSSColorConst.SKYBLUE2 = _RGBColor.to_css(
        126,
        192,
        238,
        255,
    )
    CSSColorConst.SKYBLUE3 = _RGBColor.to_css(
        108,
        166,
        205,
        255,
    )
    CSSColorConst.SKYBLUE4 = _RGBColor.to_css(
        74,
        112,
        139,
        255,
    )
    CSSColorConst.SLATEBLUE = _RGBColor.to_css(
        106,
        90,
        205,
        255,
    )
    CSSColorConst.SLATEBLUE1 = _RGBColor.to_css(
        131,
        111,
        255,
        255,
    )
    CSSColorConst.SLATEBLUE2 = _RGBColor.to_css(
        122,
        103,
        238,
        255,
    )
    CSSColorConst.SLATEBLUE3 = _RGBColor.to_css(
        105,
        89,
        205,
        255,
    )
    CSSColorConst.SLATEBLUE4 = _RGBColor.to_css(
        71,
        60,
        139,
        255,
    )
    CSSColorConst.SLATEGRAY = _RGBColor.to_css(
        112,
        128,
        144,
        255,
    )
    CSSColorConst.SLATEGRAY1 = _RGBColor.to_css(
        198,
        226,
        255,
        255,
    )
    CSSColorConst.SLATEGRAY2 = _RGBColor.to_css(
        185,
        211,
        238,
        255,
    )
    CSSColorConst.SLATEGRAY3 = _RGBColor.to_css(
        159,
        182,
        205,
        255,
    )
    CSSColorConst.SLATEGRAY4 = _RGBColor.to_css(
        108,
        123,
        139,
        255,
    )
    CSSColorConst.SNOW = _RGBColor.to_css(
        255,
        250,
        250,
        255,
    )
    CSSColorConst.SNOW2 = _RGBColor.to_css(
        238,
        233,
        233,
        255,
    )
    CSSColorConst.SNOW3 = _RGBColor.to_css(
        205,
        201,
        201,
        255,
    )
    CSSColorConst.SNOW4 = _RGBColor.to_css(
        139,
        137,
        137,
        255,
    )
    CSSColorConst.SPRINGGREEN = _RGBColor.to_css(
        0,
        255,
        127,
        255,
    )
    CSSColorConst.SPRINGGREEN2 = _RGBColor.to_css(
        0,
        238,
        118,
        255,
    )
    CSSColorConst.SPRINGGREEN3 = _RGBColor.to_css(
        0,
        205,
        102,
        255,
    )
    CSSColorConst.SPRINGGREEN4 = _RGBColor.to_css(
        0,
        139,
        69,
        255,
    )
    CSSColorConst.STEELBLUE = _RGBColor.to_css(
        70,
        130,
        180,
        255,
    )
    CSSColorConst.STEELBLUE1 = _RGBColor.to_css(
        99,
        184,
        255,
        255,
    )
    CSSColorConst.STEELBLUE2 = _RGBColor.to_css(
        92,
        172,
        238,
        255,
    )
    CSSColorConst.STEELBLUE3 = _RGBColor.to_css(
        79,
        148,
        205,
        255,
    )
    CSSColorConst.STEELBLUE4 = _RGBColor.to_css(
        54,
        100,
        139,
        255,
    )
    CSSColorConst.TAN = _RGBColor.to_css(
        210,
        180,
        140,
        255,
    )
    CSSColorConst.TAN1 = _RGBColor.to_css(
        255,
        165,
        79,
        255,
    )
    CSSColorConst.TAN2 = _RGBColor.to_css(
        238,
        154,
        73,
        255,
    )
    CSSColorConst.TAN4 = _RGBColor.to_css(
        139,
        90,
        43,
        255,
    )
    CSSColorConst.TEAL = _RGBColor.to_css(
        0,
        128,
        128,
        255,
    )
    CSSColorConst.THISTLE = _RGBColor.to_css(
        216,
        191,
        216,
        255,
    )
    CSSColorConst.THISTLE1 = _RGBColor.to_css(
        255,
        225,
        255,
        255,
    )
    CSSColorConst.THISTLE2 = _RGBColor.to_css(
        238,
        210,
        238,
        255,
    )
    CSSColorConst.THISTLE3 = _RGBColor.to_css(
        205,
        181,
        205,
        255,
    )
    CSSColorConst.THISTLE4 = _RGBColor.to_css(
        139,
        123,
        139,
        255,
    )
    CSSColorConst.TOMATO = _RGBColor.to_css(
        255,
        99,
        71,
        255,
    )
    CSSColorConst.TOMATO2 = _RGBColor.to_css(
        238,
        92,
        66,
        255,
    )
    CSSColorConst.TOMATO3 = _RGBColor.to_css(
        205,
        79,
        57,
        255,
    )
    CSSColorConst.TOMATO4 = _RGBColor.to_css(
        139,
        54,
        38,
        255,
    )
    CSSColorConst.TURQUOISE = _RGBColor.to_css(
        64,
        224,
        208,
        255,
    )
    CSSColorConst.TURQUOISE1 = _RGBColor.to_css(
        0,
        245,
        255,
        255,
    )
    CSSColorConst.TURQUOISE2 = _RGBColor.to_css(
        0,
        229,
        238,
        255,
    )
    CSSColorConst.TURQUOISE3 = _RGBColor.to_css(
        0,
        197,
        205,
        255,
    )
    CSSColorConst.TURQUOISE4 = _RGBColor.to_css(
        0,
        134,
        139,
        255,
    )
    CSSColorConst.VIOLET = _RGBColor.to_css(
        238,
        130,
        238,
        255,
    )
    CSSColorConst.VIOLETRED = _RGBColor.to_css(
        208,
        32,
        144,
        255,
    )
    CSSColorConst.VIOLETRED1 = _RGBColor.to_css(
        255,
        62,
        150,
        255,
    )
    CSSColorConst.VIOLETRED2 = _RGBColor.to_css(
        238,
        58,
        140,
        255,
    )
    CSSColorConst.VIOLETRED3 = _RGBColor.to_css(
        205,
        50,
        120,
        255,
    )
    CSSColorConst.VIOLETRED4 = _RGBColor.to_css(
        139,
        34,
        82,
        255,
    )
    CSSColorConst.WHEAT = _RGBColor.to_css(
        245,
        222,
        179,
        255,
    )
    CSSColorConst.WHEAT1 = _RGBColor.to_css(
        255,
        231,
        186,
        255,
    )
    CSSColorConst.WHEAT2 = _RGBColor.to_css(
        238,
        216,
        174,
        255,
    )
    CSSColorConst.WHEAT3 = _RGBColor.to_css(
        205,
        186,
        150,
        255,
    )
    CSSColorConst.WHEAT4 = _RGBColor.to_css(
        139,
        126,
        102,
        255,
    )
    CSSColorConst.WHITE = _RGBColor.to_css(
        255,
        255,
        255,
        255
    )
    CSSColorConst.YELLOW = _RGBColor.to_css(
        255,
        255,
        0,
        255,
    )
    CSSColorConst.YELLOW2 = _RGBColor.to_css(
        238,
        238,
        0,
        255,
    )
    CSSColorConst.YELLOW3 = _RGBColor.to_css(
        205,
        205,
        0,
        255,
    )
    CSSColorConst.YELLOW4 = _RGBColor.to_css(
        139,
        139,
        0,
        255,
    )

    @staticmethod
    def to_rgba(color: str) -> tuple:
        """
        Convert a CSS color string to RGBA tuple.

        :param color: CSS color string.
        :return: tuple: RGBA tuple.
        """
        if color.startswith('#'):
            hex_str = color[1:]
        elif color.startswith('0x'):
            hex_str = color[2:]
        else:
            hex_str = color[::]
        if len(hex_str) == 3:
            hex_str += 'F'
        elif len(hex_str) == 6:
            hex_str += 'FF'
        if len(hex_str) == 4:
            hex_str = "".join(2 * digit for digit in hex_str[:])
        return tuple(int(hex_str[i:i + 2], 16) for i in (0, 2, 4, 6))


RGBAColor = _RGBColor.RGBAColorConst
RGBAColor.to_hex_color = _RGBColor.to_css
HEXColor = _CSSColor.CSSColorConst
HEXColor.to_rgba_color = _CSSColor.to_rgba


def get_version():
    """Returns the current version number of the pygwidgets package"""
    return __version__


class TestCase(unittest.TestCase):
    def test_get_version(self):
        self.assertEqual(get_version(), __version__)

    def test_hexcolor(self):
        self.assertEqual(HEXColor.RED, '#FF0000FF')
        with self.assertRaisesRegex(ConstantError, 'Cannot change the value of the Type Constant!'):
            HEXColor.BLUE = '#'
        self.assertEqual(HEXColor.YELLOW, '#FFFF00FF')
        self.assertEqual(HEXColor.to_rgba_color(HEXColor.RED), (255, 0, 0, 255))
        self.assertEqual(HEXColor.to_rgba_color('#F0F'), (255, 0, 255, 255))
        self.assertEqual(HEXColor.to_rgba_color('#F00F'), (255, 0, 0, 255))
        self.assertEqual(HEXColor.to_rgba_color('0xFF00FF'), (255, 0, 255, 255))
        self.assertEqual(HEXColor.to_rgba_color('#FF02FFFC'), (255, 2, 255, 252))

    def test_rgbacolor(self):
        self.assertEqual(RGBAColor.RED, (255, 0, 0, 255))
        self.assertEqual(RGBAColor.BLUE, (0, 0, 255, 255))
        with self.assertRaisesRegex(ConstantError, 'Cannot change the value of the Type Constant!'):
            RGBAColor.RED = (255, 1, 1, 255)
        self.assertEqual(RGBAColor.to_hex_color(RGBAColor.BLUE), HEXColor.BLUE)
        self.assertEqual(RGBAColor.to_hex_color(RGBAColor.YELLOW), HEXColor.YELLOW)


if __name__ == '__main__':
    unittest.main()
