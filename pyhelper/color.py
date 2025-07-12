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

from pyhelper import Singleton

__all__ = [
    "RGBColor",
    "HSLColor",
    "HEXColor",
]


class _RGBColor(Singleton):
    def __init__(self):
        self.ALICE_BLUE = (
            240,
            248,
            255,
            255,
        )[:3]
        self.ANTIQUE_WHITE = (
            250,
            235,
            215,
            255,
        )[:3]
        self.ANTIQUE_WHITE1 = (
            255,
            239,
            219,
            255,
        )[:3]
        self.ANTIQUE_WHITE2 = (
            238,
            223,
            204,
            255,
        )[:3]
        self.ANTIQUE_WHITE3 = (
            205,
            192,
            176,
            255,
        )[:3]
        self.ANTIQUE_WHITE4 = (
            139,
            131,
            120,
            255,
        )[:3]
        self.AQUA = (
            0,
            255,
            255,
            255,
        )[:3]
        self.AQUAMARINE = (
            127,
            255,
            212,
            255,
        )[:3]
        self.AQUAMARINE2 = (
            118,
            238,
            198,
            255,
        )[:3]
        self.AQUAMARINE3 = (
            102,
            205,
            170,
            255,
        )[:3]
        self.AQUAMARINE4 = (
            69,
            139,
            116,
            255,
        )[:3]
        self.AZURE = (
            240,
            255,
            255,
            255,
        )[:3]
        self.AZURE2 = (
            224,
            238,
            238,
            255,
        )[:3]
        self.AZURE3 = (
            193,
            205,
            205,
            255,
        )[:3]
        self.AZURE4 = (
            131,
            139,
            139,
            255,
        )[:3]
        self.BEIGE = (
            245,
            245,
            220,
            255,
        )[:3]
        self.BISQUE = (
            255,
            228,
            196,
            255,
        )[:3]
        self.BISQUE2 = (
            238,
            213,
            183,
            255,
        )[:3]
        self.BISQUE3 = (
            205,
            183,
            158,
            255,
        )[:3]
        self.BISQUE4 = (
            139,
            125,
            107,
            255,
        )[:3]
        self.BLACK = (
            0,
            0,
            0,
            255,
        )[:3]
        self.BLANCHED_ALMOND = (
            255,
            235,
            205,
            255,
        )[:3]
        self.BLUE = (
            0,
            0,
            255,
            255,
        )[:3]
        self.BLUE2 = (
            0,
            0,
            238,
            255,
        )[:3]
        self.BLUE3 = (
            0,
            0,
            205,
            255,
        )[:3]
        self.BLUE4 = (
            0,
            0,
            139,
            255,
        )[:3]
        self.BLUE_VIOLET = (
            138,
            43,
            226,
            255,
        )[:3]
        self.BROWN = (
            165,
            42,
            42,
            255,
        )[:3]
        self.BROWN1 = (
            255,
            64,
            64,
            255,
        )[:3]
        self.BROWN2 = (
            238,
            59,
            59,
            255,
        )[:3]
        self.BROWN3 = (
            205,
            51,
            51,
            255,
        )[:3]
        self.BROWN4 = (
            139,
            35,
            35,
            255,
        )[:3]
        self.BURLY_WOOD = (
            222,
            184,
            135,
            255,
        )[:3]
        self.BURLY_WOOD1 = (
            255,
            211,
            155,
            255,
        )[:3]
        self.BURLY_WOOD2 = (
            238,
            197,
            145,
            255,
        )[:3]
        self.BURLY_WOOD3 = (
            205,
            170,
            125,
            255,
        )[:3]
        self.BURLY_WOOD4 = (
            139,
            115,
            85,
            255,
        )[:3]
        self.CADET_BLUE = (
            95,
            158,
            160,
            255,
        )[:3]
        self.CADET_BLUE1 = (
            152,
            245,
            255,
            255,
        )[:3]
        self.CADET_BLUE2 = (
            142,
            229,
            238,
            255,
        )[:3]
        self.CADET_BLUE3 = (
            122,
            197,
            205,
            255,
        )[:3]
        self.CADET_BLUE4 = (
            83,
            134,
            139,
            255,
        )[:3]
        self.CHARTREUSE = (
            127,
            255,
            0,
            255,
        )[:3]
        self.CHARTREUSE2 = (
            118,
            238,
            0,
            255,
        )[:3]
        self.CHARTREUSE3 = (
            102,
            205,
            0,
            255,
        )[:3]
        self.CHARTREUSE4 = (
            69,
            139,
            0,
            255,
        )[:3]
        self.CHOCOLATE = (
            210,
            105,
            30,
            255,
        )[:3]
        self.CHOCOLATE1 = (
            255,
            127,
            36,
            255,
        )[:3]
        self.CHOCOLATE2 = (
            238,
            118,
            33,
            255,
        )[:3]
        self.CHOCOLATE3 = (
            205,
            102,
            29,
            255,
        )[:3]
        self.CHOCOLATE4 = (
            139,
            69,
            19,
            255,
        )[:3]
        self.CORAL = (
            255,
            127,
            80,
            255,
        )[:3]
        self.CORAL1 = (
            255,
            114,
            86,
            255,
        )[:3]
        self.CORAL2 = (
            238,
            106,
            80,
            255,
        )[:3]
        self.CORAL3 = (
            205,
            91,
            69,
            255,
        )[:3]
        self.CORAL4 = (
            139,
            62,
            47,
            255,
        )[:3]
        self.CORNFLOWER_BLUE = (
            100,
            149,
            237,
            255,
        )[:3]
        self.CORN_SILK = (
            255,
            248,
            220,
            255,
        )[:3]
        self.CORN_SILK2 = (
            238,
            232,
            205,
            255,
        )[:3]
        self.CORN_SILK3 = (
            205,
            200,
            177,
            255,
        )[:3]
        self.CORN_SILK4 = (
            139,
            136,
            120,
            255,
        )[:3]
        self.CRIMSON = (
            220,
            20,
            60,
            255,
        )[:3]
        self.CYAN2 = (
            0,
            238,
            238,
            255,
        )[:3]
        self.CYAN3 = (
            0,
            205,
            205,
            255,
        )[:3]
        self.CYAN4 = (
            0,
            139,
            139,
            255,
        )[:3]
        self.DARK_GOLDENROD = (
            184,
            134,
            11,
            255,
        )[:3]
        self.DARK_GOLDENROD1 = (
            255,
            185,
            15,
            255,
        )[:3]
        self.DARK_GOLDENROD2 = (
            238,
            173,
            14,
            255,
        )[:3]
        self.DARK_GOLDENROD3 = (
            205,
            149,
            12,
            255,
        )[:3]
        self.DARK_GOLDENROD4 = (
            139,
            101,
            8,
            255,
        )[:3]
        self.DARK_GRAY = (
            169,
            169,
            169,
            255,
        )[:3]
        self.DARK_GREEN = (
            0,
            100,
            0,
            255,
        )[:3]
        self.DARK_KHAKI = (
            189,
            183,
            107,
            255,
        )[:3]
        self.DARK_MAGENTA = (
            139,
            0,
            139,
            255,
        )[:3]
        self.DARK_OLIVE_GREEN = (
            85,
            107,
            47,
            255,
        )[:3]
        self.DARK_OLIVE_GREEN1 = (
            202,
            255,
            112,
            255,
        )[:3]
        self.DARK_OLIVE_GREEN2 = (
            188,
            238,
            104,
            255,
        )[:3]
        self.DARK_OLIVE_GREEN3 = (
            162,
            205,
            90,
            255,
        )[:3]
        self.DARK_OLIVE_GREEN4 = (
            110,
            139,
            61,
            255,
        )[:3]
        self.DARK_ORANGE = (
            255,
            140,
            0,
            255,
        )[:3]
        self.DARK_ORANGE1 = (
            255,
            127,
            0,
            255,
        )[:3]
        self.DARK_ORANGE2 = (
            238,
            118,
            0,
            255,
        )[:3]
        self.DARK_ORANGE3 = (
            205,
            102,
            0,
            255,
        )[:3]
        self.DARK_ORANGE4 = (
            139,
            69,
            0,
            255,
        )[:3]
        self.DARK_ORCHID = (
            153,
            50,
            204,
            255,
        )[:3]
        self.DARK_ORCHID1 = (
            191,
            62,
            255,
            255,
        )[:3]
        self.DARK_ORCHID2 = (
            178,
            58,
            238,
            255,
        )[:3]
        self.DARK_ORCHID3 = (
            154,
            50,
            205,
            255,
        )[:3]
        self.DARK_ORCHID4 = (
            104,
            34,
            139,
            255,
        )[:3]
        self.DARK_RED = (
            139,
            0,
            0,
            255,
        )[:3]
        self.DARK_SALMON = (
            233,
            150,
            122,
            255,
        )[:3]
        self.DARK_SEA_GREEN = (
            143,
            188,
            143,
            255,
        )[:3]
        self.DARK_SEA_GREEN1 = (
            193,
            255,
            193,
            255,
        )[:3]
        self.DARK_SEA_GREEN2 = (
            180,
            238,
            180,
            255,
        )[:3]
        self.DARK_SEA_GREEN3 = (
            155,
            205,
            155,
            255,
        )[:3]
        self.DARK_SEA_GREEN4 = (
            105,
            139,
            105,
            255,
        )[:3]
        self.DARK_SLATE_BLUE = (
            72,
            61,
            139,
            255,
        )[:3]
        self.DARK_SLATE_GRAY = (
            47,
            79,
            79,
            255,
        )[:3]
        self.DARK_SLATE_GRAY1 = (
            151,
            255,
            255,
            255,
        )[:3]
        self.DARK_SLATE_GRAY2 = (
            141,
            238,
            238,
            255,
        )[:3]
        self.DARK_SLATE_GRAY3 = (
            121,
            205,
            205,
            255,
        )[:3]
        self.DARK_SLATE_GRAY4 = (
            82,
            139,
            139,
            255,
        )[:3]
        self.DARK_TURQUOISE = (
            0,
            206,
            209,
            255,
        )[:3]
        self.DARK_VIOLET = (
            148,
            0,
            211,
            255,
        )[:3]
        self.DEEP_PINK = (
            255,
            20,
            147,
            255,
        )[:3]
        self.DEEP_PINK2 = (
            238,
            18,
            137,
            255,
        )[:3]
        self.DEEP_PINK3 = (
            205,
            16,
            118,
            255,
        )[:3]
        self.DEEP_PINK4 = (
            139,
            10,
            80,
            255,
        )[:3]
        self.DEEP_SKY_BLUE = (
            0,
            191,
            255,
            255,
        )[:3]
        self.DEEP_SKY_BLUE2 = (
            0,
            178,
            238,
            255,
        )[:3]
        self.DEEP_SKY_BLUE3 = (
            0,
            154,
            205,
            255,
        )[:3]
        self.DEEP_SKY_BLUE4 = (
            0,
            104,
            139,
            255,
        )[:3]
        self.DIM_GRAY = (
            105,
            105,
            105,
            255,
        )[:3]
        self.DODGER_BLUE = (
            30,
            144,
            255,
            255,
        )[:3]
        self.DODGER_BLUE2 = (
            28,
            134,
            238,
            255,
        )[:3]
        self.DODGER_BLUE3 = (
            24,
            116,
            205,
            255,
        )[:3]
        self.DODGER_BLUE4 = (
            16,
            78,
            139,
            255,
        )[:3]
        self.FIRE_BRICK = (
            178,
            34,
            34,
            255,
        )[:3]
        self.FIRE_BRICK1 = (
            255,
            48,
            48,
            255,
        )[:3]
        self.FIRE_BRICK2 = (
            238,
            44,
            44,
            255,
        )[:3]
        self.FIRE_BRICK3 = (
            205,
            38,
            38,
            255,
        )[:3]
        self.FIRE_BRICK4 = (
            139,
            26,
            26,
            255,
        )[:3]
        self.FLORAL_WHITE = (
            255,
            250,
            240,
            255,
        )[:3]
        self.FOREST_GREEN = (
            34,
            139,
            34,
            255,
        )[:3]
        self.FUCHSIA = (
            255,
            0,
            255,
            255,
        )[:3]
        self.GAINSBORO = (
            220,
            220,
            220,
            255,
        )[:3]
        self.GHOST_WHITE = (
            248,
            248,
            255,
            255,
        )[:3]
        self.GOLD = (
            255,
            215,
            0,
            255,
        )[:3]
        self.GOLD2 = (
            238,
            201,
            0,
            255,
        )[:3]
        self.GOLD3 = (
            205,
            173,
            0,
            255,
        )[:3]
        self.GOLD4 = (
            139,
            117,
            0,
            255,
        )[:3]
        self.GOLDENROD = (
            218,
            165,
            32,
            255,
        )[:3]
        self.GOLDENROD1 = (
            255,
            193,
            37,
            255,
        )[:3]
        self.GOLDENROD2 = (
            238,
            180,
            34,
            255,
        )[:3]
        self.GOLDENROD3 = (
            205,
            155,
            29,
            255,
        )[:3]
        self.GOLDENROD4 = (
            139,
            105,
            20,
            255,
        )[:3]
        self.GRAY = (
            190,
            190,
            190,
            255,
        )[:3]
        self.GRAY1 = (
            3,
            3,
            3,
            255,
        )[:3]
        self.GRAY10 = (
            26,
            26,
            26,
            255,
        )[:3]
        self.GRAY100 = (
            255,
            255,
            255,
            255,
        )[:3]
        self.GRAY11 = (
            28,
            28,
            28,
            255,
        )[:3]
        self.GRAY12 = (
            31,
            31,
            31,
            255,
        )[:3]
        self.GRAY13 = (
            33,
            33,
            33,
            255,
        )[:3]
        self.GRAY14 = (
            36,
            36,
            36,
            255,
        )[:3]
        self.GRAY15 = (
            38,
            38,
            38,
            255,
        )[:3]
        self.GRAY16 = (
            41,
            41,
            41,
            255,
        )[:3]
        self.GRAY17 = (
            43,
            43,
            43,
            255,
        )[:3]
        self.GRAY18 = (
            46,
            46,
            46,
            255,
        )[:3]
        self.GRAY19 = (
            48,
            48,
            48,
            255,
        )[:3]
        self.GRAY2 = (
            5,
            5,
            5,
            255,
        )[:3]
        self.GRAY20 = (
            51,
            51,
            51,
            255,
        )[:3]
        self.GRAY21 = (
            54,
            54,
            54,
            255,
        )[:3]
        self.GRAY22 = (
            56,
            56,
            56,
            255,
        )[:3]
        self.GRAY23 = (
            59,
            59,
            59,
            255,
        )[:3]
        self.GRAY24 = (
            61,
            61,
            61,
            255,
        )[:3]
        self.GRAY25 = (
            64,
            64,
            64,
            255,
        )[:3]
        self.GRAY26 = (
            66,
            66,
            66,
            255,
        )[:3]
        self.GRAY27 = (
            69,
            69,
            69,
            255,
        )[:3]
        self.GRAY28 = (
            71,
            71,
            71,
            255,
        )[:3]
        self.GRAY29 = (
            74,
            74,
            74,
            255,
        )[:3]
        self.GRAY3 = (
            8,
            8,
            8,
            255,
        )[:3]
        self.GRAY30 = (
            77,
            77,
            77,
            255,
        )[:3]
        self.GRAY31 = (
            79,
            79,
            79,
            255,
        )[:3]
        self.GRAY32 = (
            82,
            82,
            82,
            255,
        )[:3]
        self.GRAY33 = (
            84,
            84,
            84,
            255,
        )[:3]
        self.GRAY34 = (
            87,
            87,
            87,
            255,
        )[:3]
        self.GRAY35 = (
            89,
            89,
            89,
            255,
        )[:3]
        self.GRAY36 = (
            92,
            92,
            92,
            255,
        )[:3]
        self.GRAY37 = (
            94,
            94,
            94,
            255,
        )[:3]
        self.GRAY38 = (
            97,
            97,
            97,
            255,
        )[:3]
        self.GRAY39 = (
            99,
            99,
            99,
            255,
        )[:3]
        self.GRAY4 = (
            10,
            10,
            10,
            255,
        )[:3]
        self.GRAY40 = (
            102,
            102,
            102,
            255,
        )[:3]
        self.GRAY42 = (
            107,
            107,
            107,
            255,
        )[:3]
        self.GRAY43 = (
            110,
            110,
            110,
            255,
        )[:3]
        self.GRAY44 = (
            112,
            112,
            112,
            255,
        )[:3]
        self.GRAY45 = (
            115,
            115,
            115,
            255,
        )[:3]
        self.GRAY46 = (
            117,
            117,
            117,
            255,
        )[:3]
        self.GRAY47 = (
            120,
            120,
            120,
            255,
        )[:3]
        self.GRAY48 = (
            122,
            122,
            122,
            255,
        )[:3]
        self.GRAY49 = (
            125,
            125,
            125,
            255,
        )[:3]
        self.GRAY5 = (
            13,
            13,
            13,
            255,
        )[:3]
        self.GRAY50 = (
            127,
            127,
            127,
            255,
        )[:3]
        self.GRAY51 = (
            130,
            130,
            130,
            255,
        )[:3]
        self.GRAY52 = (
            133,
            133,
            133,
            255,
        )[:3]
        self.GRAY53 = (
            135,
            135,
            135,
            255,
        )[:3]
        self.GRAY54 = (
            138,
            138,
            138,
            255,
        )[:3]
        self.GRAY55 = (
            140,
            140,
            140,
            255,
        )[:3]
        self.GRAY56 = (
            143,
            143,
            143,
            255,
        )[:3]
        self.GRAY57 = (
            145,
            145,
            145,
            255,
        )[:3]
        self.GRAY58 = (
            148,
            148,
            148,
            255,
        )[:3]
        self.GRAY59 = (
            150,
            150,
            150,
            255,
        )[:3]
        self.GRAY6 = (
            15,
            15,
            15,
            255,
        )[:3]
        self.GRAY60 = (
            153,
            153,
            153,
            255,
        )[:3]
        self.GRAY61 = (
            156,
            156,
            156,
            255,
        )[:3]
        self.GRAY62 = (
            158,
            158,
            158,
            255,
        )[:3]
        self.GRAY63 = (
            161,
            161,
            161,
            255,
        )[:3]
        self.GRAY64 = (
            163,
            163,
            163,
            255,
        )[:3]
        self.GRAY65 = (
            166,
            166,
            166,
            255,
        )[:3]
        self.GRAY66 = (
            168,
            168,
            168,
            255,
        )[:3]
        self.GRAY67 = (
            171,
            171,
            171,
            255,
        )[:3]
        self.GRAY68 = (
            173,
            173,
            173,
            255,
        )[:3]
        self.GRAY69 = (
            176,
            176,
            176,
            255,
        )[:3]
        self.GRAY7 = (
            18,
            18,
            18,
            255,
        )[:3]
        self.GRAY70 = (
            179,
            179,
            179,
            255,
        )[:3]
        self.GRAY71 = (
            181,
            181,
            181,
            255,
        )[:3]
        self.GRAY72 = (
            184,
            184,
            184,
            255,
        )[:3]
        self.GRAY73 = (
            186,
            186,
            186,
            255,
        )[:3]
        self.GRAY74 = (
            189,
            189,
            189,
            255,
        )[:3]
        self.GRAY75 = (
            191,
            191,
            191,
            255,
        )[:3]
        self.GRAY76 = (
            194,
            194,
            194,
            255,
        )[:3]
        self.GRAY77 = (
            196,
            196,
            196,
            255,
        )[:3]
        self.GRAY78 = (
            199,
            199,
            199,
            255,
        )[:3]
        self.GRAY79 = (
            201,
            201,
            201,
            255,
        )[:3]
        self.GRAY8 = (
            20,
            20,
            20,
            255,
        )[:3]
        self.GRAY80 = (
            204,
            204,
            204,
            255,
        )[:3]
        self.GRAY81 = (
            207,
            207,
            207,
            255,
        )[:3]
        self.GRAY82 = (
            209,
            209,
            209,
            255,
        )[:3]
        self.GRAY83 = (
            212,
            212,
            212,
            255,
        )[:3]
        self.GRAY84 = (
            214,
            214,
            214,
            255,
        )[:3]
        self.GRAY85 = (
            217,
            217,
            217,
            255,
        )[:3]
        self.GRAY86 = (
            219,
            219,
            219,
            255,
        )[:3]
        self.GRAY87 = (
            222,
            222,
            222,
            255,
        )[:3]
        self.GRAY88 = (
            224,
            224,
            224,
            255,
        )[:3]
        self.GRAY89 = (
            227,
            227,
            227,
            255,
        )[:3]
        self.GRAY9 = (
            23,
            23,
            23,
            255,
        )[:3]
        self.GRAY90 = (
            229,
            229,
            229,
            255,
        )[:3]
        self.GRAY91 = (
            232,
            232,
            232,
            255,
        )[:3]
        self.GRAY92 = (
            235,
            235,
            235,
            255,
        )[:3]
        self.GRAY93 = (
            237,
            237,
            237,
            255,
        )[:3]
        self.GRAY94 = (
            240,
            240,
            240,
            255,
        )[:3]
        self.GRAY95 = (
            242,
            242,
            242,
            255,
        )[:3]
        self.GRAY96 = (
            245,
            245,
            245,
            255,
        )[:3]
        self.GRAY97 = (
            247,
            247,
            247,
            255,
        )[:3]
        self.GRAY98 = (
            250,
            250,
            250,
            255,
        )[:3]
        self.GRAY99 = (
            252,
            252,
            252,
            255,
        )[:3]
        self.GREEN = (
            0,
            255,
            0,
            255,
        )[:3]
        self.GREEN2 = (
            0,
            238,
            0,
            255,
        )[:3]
        self.GREEN3 = (
            0,
            205,
            0,
            255,
        )[:3]
        self.GREEN4 = (
            0,
            139,
            0,
            255,
        )[:3]
        self.GREEN_YELLOW = (
            173,
            255,
            47,
            255,
        )[:3]
        self.HONEYDEW = (
            240,
            255,
            240,
            255,
        )[:3]
        self.HONEYDEW2 = (
            224,
            238,
            224,
            255,
        )[:3]
        self.HONEYDEW3 = (
            193,
            205,
            193,
            255,
        )[:3]
        self.HONEYDEW4 = (
            131,
            139,
            131,
            255,
        )[:3]
        self.HOT_PINK = (
            255,
            105,
            180,
            255,
        )[:3]
        self.HOT_PINK1 = (
            255,
            110,
            180,
            255,
        )[:3]
        self.HOT_PINK2 = (
            238,
            106,
            167,
            255,
        )[:3]
        self.HOT_PINK3 = (
            205,
            96,
            144,
            255,
        )[:3]
        self.HOT_PINK4 = (
            139,
            58,
            98,
            255,
        )[:3]
        self.INDIAN_RED = (
            205,
            92,
            92,
            255,
        )[:3]
        self.INDIAN_RED1 = (
            255,
            106,
            106,
            255,
        )[:3]
        self.INDIAN_RED2 = (
            238,
            99,
            99,
            255,
        )[:3]
        self.INDIAN_RED3 = (
            205,
            85,
            85,
            255,
        )[:3]
        self.INDIAN_RED4 = (
            139,
            58,
            58,
            255,
        )[:3]
        self.INDIGO = (
            75,
            0,
            130,
            255,
        )[:3]
        self.IVORY = (
            255,
            255,
            240,
            255,
        )[:3]
        self.IVORY2 = (
            238,
            238,
            224,
            255,
        )[:3]
        self.IVORY3 = (
            205,
            205,
            193,
            255,
        )[:3]
        self.IVORY4 = (
            139,
            139,
            131,
            255,
        )[:3]
        self.KHAKI = (
            240,
            230,
            140,
            255,
        )[:3]
        self.KHAKI1 = (
            255,
            246,
            143,
            255,
        )[:3]
        self.KHAKI2 = (
            238,
            230,
            133,
            255,
        )[:3]
        self.KHAKI3 = (
            205,
            198,
            115,
            255,
        )[:3]
        self.KHAKI4 = (
            139,
            134,
            78,
            255,
        )[:3]
        self.LAVENDER = (
            230,
            230,
            250,
            255,
        )[:3]
        self.LAVENDER_BLUSH = (
            255,
            240,
            245,
            255,
        )[:3]
        self.LAVENDER_BLUSH2 = (
            238,
            224,
            229,
            255,
        )[:3]
        self.LAVENDER_BLUSH3 = (
            205,
            193,
            197,
            255,
        )[:3]
        self.LAVENDER_BLUSH4 = (
            139,
            131,
            134,
            255,
        )[:3]
        self.LAWN_GREEN = (
            124,
            252,
            0,
            255,
        )[:3]
        self.LEMONCHIFFON = (
            255,
            250,
            205,
            255,
        )[:3]
        self.LEMONCHIFFON2 = (
            238,
            233,
            191,
            255,
        )[:3]
        self.LEMONCHIFFON3 = (
            205,
            201,
            165,
            255,
        )[:3]
        self.LEMONCHIFFON4 = (
            139,
            137,
            112,
            255,
        )[:3]
        self.LIGHT_BLUE = (
            173,
            216,
            230,
            255,
        )[:3]
        self.LIGHT_BLUE1 = (
            191,
            239,
            255,
            255,
        )[:3]
        self.LIGHT_BLUE2 = (
            178,
            223,
            238,
            255,
        )[:3]
        self.LIGHT_BLUE3 = (
            154,
            192,
            205,
            255,
        )[:3]
        self.LIGHT__BLUE4 = (
            104,
            131,
            139,
            255,
        )[:3]
        self.LIGHT_CORAL = (
            240,
            128,
            128,
            255,
        )[:3]
        self.LIGHT_CYAN = (
            224,
            255,
            255,
            255,
        )[:3]
        self.LIGHT_CYAN2 = (
            209,
            238,
            238,
            255,
        )[:3]
        self.LIGHT_CYAN3 = (
            180,
            205,
            205,
            255,
        )[:3]
        self.LIGHT_CYAN4 = (
            122,
            139,
            139,
            255,
        )[:3]
        self.LIGHT_GOLDENROD = (
            238,
            221,
            130,
            255,
        )[:3]
        self.LIGHT_GOLDENROD1 = (
            255,
            236,
            139,
            255,
        )[:3]
        self.LIGHT_GOLDENROD2 = (
            238,
            220,
            130,
            255,
        )[:3]
        self.LIGHT_GOLDENROD3 = (
            205,
            190,
            112,
            255,
        )[:3]
        self.LIGHT_GOLDENROD4 = (
            139,
            129,
            76,
            255,
        )[:3]
        self.LIGHT_GOLDENROD_YELLOW = (
            250,
            250,
            210,
            255,
        )[:3]
        self.LIGHT_GRAY = (
            211,
            211,
            211,
            255,
        )[:3]
        self.LIGHT_GREEN = (
            144,
            238,
            144,
            255,
        )[:3]
        self.LIGHT_PINK = (
            255,
            182,
            193,
            255,
        )[:3]
        self.LIGHT_PINK1 = (
            255,
            174,
            185,
            255,
        )[:3]
        self.LIGHT_PINK2 = (
            238,
            162,
            173,
            255,
        )[:3]
        self.LIGHT_PINK3 = (
            205,
            140,
            149,
            255,
        )[:3]
        self.LIGHT_PINK4 = (
            139,
            95,
            101,
            255,
        )[:3]
        self.LIGHT_SALMON = (
            255,
            160,
            122,
            255,
        )[:3]
        self.LIGHT_SALMON2 = (
            238,
            149,
            114,
            255,
        )[:3]
        self.LIGHT_SALMON3 = (
            205,
            129,
            98,
            255,
        )[:3]
        self.LIGHT_SALMON4 = (
            139,
            87,
            66,
            255,
        )[:3]
        self.LIGHT_SEA_GREEN = (
            32,
            178,
            170,
            255,
        )[:3]
        self.LIGHT_SKY_BLUE = (
            135,
            206,
            250,
            255,
        )[:3]
        self.LIGHT_SKY_BLUE1 = (
            176,
            226,
            255,
            255,
        )[:3]
        self.LIGHT_SKY_BLUE2 = (
            164,
            211,
            238,
            255,
        )[:3]
        self.LIGHT_SKY_BLUE3 = (
            141,
            182,
            205,
            255,
        )[:3]
        self.LIGHT_SKY_BLUE4 = (
            96,
            123,
            139,
            255,
        )[:3]
        self.LIGHT_SLATE_BLUE = (
            132,
            112,
            255,
            255,
        )[:3]
        self.LIGHT_SLATE_GRAY = (
            119,
            136,
            153,
            255,
        )[:3]
        self.LIGHT_STEEL_BLUE = (
            176,
            196,
            222,
            255,
        )[:3]
        self.LIGHT_STEEL_BLUE1 = (
            202,
            225,
            255,
            255,
        )[:3]
        self.LIGHT_STEEL_BLUE2 = (
            188,
            210,
            238,
            255,
        )[:3]
        self.LIGHT_STEEL_BLUE3 = (
            162,
            181,
            205,
            255,
        )[:3]
        self.LIGHT_STEEL_BLUE4 = (
            110,
            123,
            139,
            255,
        )[:3]
        self.LIGHT_YELLOW = (
            255,
            255,
            224,
            255,
        )[:3]
        self.LIGHT_YELLOW2 = (
            238,
            238,
            209,
            255,
        )[:3]
        self.LIGHT_YELLOW3 = (
            205,
            205,
            180,
            255,
        )[:3]
        self.LIGHT_YELLOW4 = (
            139,
            139,
            122,
            255,
        )[:3]
        self.LIME_GREEN = (
            50,
            205,
            50,
            255,
        )[:3]
        self.LINEN = (
            250,
            240,
            230,
            255,
        )[:3]
        self.MAGENTA2 = (
            238,
            0,
            238,
            255,
        )[:3]
        self.MAGENTA3 = (
            205,
            0,
            205,
            255,
        )[:3]
        self.MAROON = (
            176,
            48,
            96,
            255,
        )[:3]
        self.MAROON1 = (
            255,
            52,
            179,
            255,
        )[:3]
        self.MAROON2 = (
            238,
            48,
            167,
            255,
        )[:3]
        self.MAROON3 = (
            205,
            41,
            144,
            255,
        )[:3]
        self.MAROON4 = (
            139,
            28,
            98,
            255,
        )[:3]
        self.MEDIUM_ORCHID = (
            186,
            85,
            211,
            255,
        )[:3]
        self.MEDIUM_ORCHID1 = (
            224,
            102,
            255,
            255,
        )[:3]
        self.MEDIUM_ORCHID2 = (
            209,
            95,
            238,
            255,
        )[:3]
        self.MEDIUM_ORCHID3 = (
            180,
            82,
            205,
            255,
        )[:3]
        self.MEDIUM_ORCHID4 = (
            122,
            55,
            139,
            255,
        )[:3]
        self.MEDIUM_PURPLE = (
            147,
            112,
            219,
            255,
        )[:3]
        self.MEDIUM_PURPLE1 = (
            171,
            130,
            255,
            255,
        )[:3]
        self.MEDIUM_PURPLE2 = (
            159,
            121,
            238,
            255,
        )[:3]
        self.MEDIUM_PURPLE3 = (
            137,
            104,
            205,
            255,
        )[:3]
        self.MEDIUM_PURPLE4 = (
            93,
            71,
            139,
            255,
        )[:3]
        self.MEDIUM_SEA_GREEN = (
            60,
            179,
            113,
            255,
        )[:3]
        self.MEDIUM_SLATE_BLUE = (
            123,
            104,
            238,
            255,
        )[:3]
        self.MEDIUM_SPRING_GREEN = (
            0,
            250,
            154,
            255,
        )[:3]
        self.MEDIUM_TURQUOISE = (
            72,
            209,
            204,
            255,
        )[:3]
        self.MEDIUM_VIOLET_RED = (
            199,
            21,
            133,
            255,
        )[:3]
        self.MIDNIGHT_BLUE = (
            25,
            25,
            112,
            255,
        )[:3]
        self.MINTCREAM = (
            245,
            255,
            250,
            255,
        )[:3]
        self.MISTY_ROSE = (
            255,
            228,
            225,
            255,
        )[:3]
        self.MISTY_ROSE2 = (
            238,
            213,
            210,
            255,
        )[:3]
        self.MISTY_ROSE3 = (
            205,
            183,
            181,
            255,
        )[:3]
        self.MISTY_ROSE4 = (
            139,
            125,
            123,
            255,
        )[:3]
        self.MOCCASIN = (
            255,
            228,
            181,
            255,
        )[:3]
        self.NAVAJO_WHITE = (
            255,
            222,
            173,
            255,
        )[:3]
        self.NAVAJO_WHITE2 = (
            238,
            207,
            161,
            255,
        )[:3]
        self.NAVAJO_WHITE3 = (
            205,
            179,
            139,
            255,
        )[:3]
        self.NAVAJO_WHITE4 = (
            139,
            121,
            94,
            255,
        )[:3]
        self.NAVY = (
            0,
            0,
            128,
            255,
        )[:3]
        self.OLD_LACE = (
            253,
            245,
            230,
            255,
        )[:3]
        self.OLIVE = (
            128,
            128,
            0,
            255,
        )[:3]
        self.OLIVE_DRAB = (
            107,
            142,
            35,
            255,
        )[:3]
        self.OLIVE_DRAB1 = (
            192,
            255,
            62,
            255,
        )[:3]
        self.OLIVE_DRAB2 = (
            179,
            238,
            58,
            255,
        )[:3]
        self.OLIVE_DRAB3 = (
            154,
            205,
            50,
            255,
        )[:3]
        self.OLIVE_DRAB4 = (
            105,
            139,
            34,
            255,
        )[:3]
        self.ORANGE = (
            255,
            165,
            0,
            255,
        )[:3]
        self.ORANGE2 = (
            238,
            154,
            0,
            255,
        )[:3]
        self.ORANGE3 = (
            205,
            133,
            0,
            255,
        )[:3]
        self.ORANGE4 = (
            139,
            90,
            0,
            255,
        )[:3]
        self.ORANGE_RED = (
            255,
            69,
            0,
            255,
        )[:3]
        self.ORANGE_RED2 = (
            238,
            64,
            0,
            255,
        )[:3]
        self.ORANGE_RED3 = (
            205,
            55,
            0,
            255,
        )[:3]
        self.ORANGE_RED4 = (
            139,
            37,
            0,
            255,
        )[:3]
        self.ORCHID = (
            218,
            112,
            214,
            255,
        )[:3]
        self.ORCHID1 = (
            255,
            131,
            250,
            255,
        )[:3]
        self.ORCHID2 = (
            238,
            122,
            233,
            255,
        )[:3]
        self.ORCHID3 = (
            205,
            105,
            201,
            255,
        )[:3]
        self.ORCHID4 = (
            139,
            71,
            137,
            255,
        )[:3]
        self.PALE_GOLDENROD = (
            238,
            232,
            170,
            255,
        )[:3]
        self.PALE_GREEN = (
            152,
            251,
            152,
            255,
        )[:3]
        self.PALE_GREEN1 = (
            154,
            255,
            154,
            255,
        )[:3]
        self.PALE_GREEN3 = (
            124,
            205,
            124,
            255,
        )[:3]
        self.PALE_GREEN4 = (
            84,
            139,
            84,
            255,
        )[:3]
        self.PALE_TURQUOISE = (
            175,
            238,
            238,
            255,
        )[:3]
        self.PALE_TURQUOISE1 = (
            187,
            255,
            255,
            255,
        )[:3]
        self.PALE_TURQUOISE2 = (
            174,
            238,
            238,
            255,
        )[:3]
        self.PALE_TURQUOISE3 = (
            150,
            205,
            205,
            255,
        )[:3]
        self.PALE_TURQUOISE4 = (
            102,
            139,
            139,
            255,
        )[:3]
        self.PALE_VIOLET_RED = (
            219,
            112,
            147,
            255,
        )[:3]
        self.PALE_VIOLET_RED1 = (
            255,
            130,
            171,
            255,
        )[:3]
        self.PALE_VIOLET_RED2 = (
            238,
            121,
            159,
            255,
        )[:3]
        self.PALE_VIOLET_RED3 = (
            205,
            104,
            137,
            255,
        )[:3]
        self.PALE_VIOLET_RED4 = (
            139,
            71,
            93,
            255,
        )[:3]
        self.PAPAYAWHIP = (
            255,
            239,
            213,
            255,
        )[:3]
        self.PEACH_PUFF = (
            255,
            218,
            185,
            255,
        )[:3]
        self.PEACH_PUFF2 = (
            238,
            203,
            173,
            255,
        )[:3]
        self.PEACH_PUFF3 = (
            205,
            175,
            149,
            255,
        )[:3]
        self.PEACH_PUFF4 = (
            139,
            119,
            101,
            255,
        )[:3]
        self.PERU = (
            205,
            133,
            63,
            255,
        )[:3]
        self.PINK = (
            255,
            192,
            203,
            255,
        )[:3]
        self.PINK1 = (
            255,
            181,
            197,
            255,
        )[:3]
        self.PINK2 = (
            238,
            169,
            184,
            255,
        )[:3]
        self.PINK3 = (
            205,
            145,
            158,
            255,
        )[:3]
        self.PINK4 = (
            139,
            99,
            108,
            255,
        )[:3]
        self.PLUM = (
            221,
            160,
            221,
            255,
        )[:3]
        self.PLUM1 = (
            255,
            187,
            255,
            255,
        )[:3]
        self.PLUM2 = (
            238,
            174,
            238,
            255,
        )[:3]
        self.PLUM3 = (
            205,
            150,
            205,
            255,
        )[:3]
        self.PLUM4 = (
            139,
            102,
            139,
            255,
        )[:3]
        self.POWDER_BLUE = (
            176,
            224,
            230,
            255,
        )[:3]
        self.PURPLE = (
            160,
            32,
            240,
            255,
        )[:3]
        self.PURPLE1 = (
            155,
            48,
            255,
            255,
        )[:3]
        self.PURPLE2 = (
            145,
            44,
            238,
            255,
        )[:3]
        self.PURPLE3 = (
            125,
            38,
            205,
            255,
        )[:3]
        self.PURPLE4 = (
            85,
            26,
            139,
            255,
        )[:3]
        self.RED = (
            255,
            0,
            0,
            255,
        )[:3]
        self.RED2 = (
            238,
            0,
            0,
            255,
        )[:3]
        self.RED3 = (
            205,
            0,
            0,
            255,
        )[:3]
        self.ROSY_BROWN = (
            188,
            143,
            143,
            255,
        )[:3]
        self.ROSY_BROWN1 = (
            255,
            193,
            193,
            255,
        )[:3]
        self.ROSY_BROWN2 = (
            238,
            180,
            180,
            255,
        )[:3]
        self.ROSY_BROWN3 = (
            205,
            155,
            155,
            255,
        )[:3]
        self.ROSY_BROWN4 = (
            139,
            105,
            105,
            255,
        )[:3]
        self.ROYAL_BLUE = (
            65,
            105,
            225,
            255,
        )[:3]
        self.ROYAL_BLUE1 = (
            72,
            118,
            255,
            255,
        )[:3]
        self.ROYAL_BLUE2 = (
            67,
            110,
            238,
            255,
        )[:3]
        self.ROYAL_BLUE3 = (
            58,
            95,
            205,
            255,
        )[:3]
        self.ROYAL_BLUE4 = (
            39,
            64,
            139,
            255,
        )[:3]
        self.SALMON = (
            250,
            128,
            114,
            255,
        )[:3]
        self.SALMON1 = (
            255,
            140,
            105,
            255,
        )[:3]
        self.SALMON2 = (
            238,
            130,
            98,
            255,
        )[:3]
        self.SALMON3 = (
            205,
            112,
            84,
            255,
        )[:3]
        self.SALMON4 = (
            139,
            76,
            57,
            255,
        )[:3]
        self.SANDY_BROWN = (
            244,
            164,
            96,
            255,
        )[:3]
        self.SEA_GREEN = (
            46,
            139,
            87,
            255,
        )[:3]
        self.SEA_GREEN1 = (
            84,
            255,
            159,
            255,
        )[:3]
        self.SEA_GREEN2 = (
            78,
            238,
            148,
            255,
        )[:3]
        self.SEA_GREEN3 = (
            67,
            205,
            128,
            255,
        )[:3]
        self.SEA_SHELL = (
            255,
            245,
            238,
            255,
        )[:3]
        self.SEA_SHELL2 = (
            238,
            229,
            222,
            255,
        )[:3]
        self.SEA_SHELL3 = (
            205,
            197,
            191,
            255,
        )[:3]
        self.SEA_SHELL4 = (
            139,
            134,
            130,
            255,
        )[:3]
        self.SIENNA = (
            160,
            82,
            45,
            255,
        )[:3]
        self.SIENNA1 = (
            255,
            130,
            71,
            255,
        )[:3]
        self.SIENNA2 = (
            238,
            121,
            66,
            255,
        )[:3]
        self.SIENNA3 = (
            205,
            104,
            57,
            255,
        )[:3]
        self.SIENNA4 = (
            139,
            71,
            38,
            255,
        )[:3]
        self.SILVER = (
            192,
            192,
            192,
            255,
        )[:3]
        self.SKY_BLUE = (
            135,
            206,
            235,
            255,
        )[:3]
        self.SKY_BLUE1 = (
            135,
            206,
            255,
            255,
        )[:3]
        self.SKY_BLUE2 = (
            126,
            192,
            238,
            255,
        )[:3]
        self.SKY_BLUE3 = (
            108,
            166,
            205,
            255,
        )[:3]
        self.SKY_BLUE4 = (
            74,
            112,
            139,
            255,
        )[:3]
        self.SLATE_BLUE = (
            106,
            90,
            205,
            255,
        )[:3]
        self.SLATE_BLUE1 = (
            131,
            111,
            255,
            255,
        )[:3]
        self.SLATE_BLUE2 = (
            122,
            103,
            238,
            255,
        )[:3]
        self.SLATE_BLUE3 = (
            105,
            89,
            205,
            255,
        )[:3]
        self.SLATE_BLUE4 = (
            71,
            60,
            139,
            255,
        )[:3]
        self.SLATE_GRAY = (
            112,
            128,
            144,
            255,
        )[:3]
        self.SLATE_GRAY1 = (
            198,
            226,
            255,
            255,
        )[:3]
        self.SLATE_GRAY2 = (
            185,
            211,
            238,
            255,
        )[:3]
        self.SLATE_GRAY3 = (
            159,
            182,
            205,
            255,
        )[:3]
        self.SLATE_GRAY4 = (
            108,
            123,
            139,
            255,
        )[:3]
        self.SNOW = (
            255,
            250,
            250,
            255,
        )[:3]
        self.SNOW2 = (
            238,
            233,
            233,
            255,
        )[:3]
        self.SNOW3 = (
            205,
            201,
            201,
            255,
        )[:3]
        self.SNOW4 = (
            139,
            137,
            137,
            255,
        )[:3]
        self.SPRING_GREEN = (
            0,
            255,
            127,
            255,
        )[:3]
        self.SPRING_GREEN2 = (
            0,
            238,
            118,
            255,
        )[:3]
        self.SPRING_GREEN3 = (
            0,
            205,
            102,
            255,
        )[:3]
        self.SPRING_GREEN4 = (
            0,
            139,
            69,
            255,
        )[:3]
        self.STEEL_BLUE = (
            70,
            130,
            180,
            255,
        )[:3]
        self.STEEL_BLUE1 = (
            99,
            184,
            255,
            255,
        )[:3]
        self.STEEL_BLUE2 = (
            92,
            172,
            238,
            255,
        )[:3]
        self.STEEL_BLUE3 = (
            79,
            148,
            205,
            255,
        )[:3]
        self.STEEL_BLUE4 = (
            54,
            100,
            139,
            255,
        )[:3]
        self.TAN = (
            210,
            180,
            140,
            255,
        )[:3]
        self.TAN1 = (
            255,
            165,
            79,
            255,
        )[:3]
        self.TAN2 = (
            238,
            154,
            73,
            255,
        )[:3]
        self.TAN4 = (
            139,
            90,
            43,
            255,
        )[:3]
        self.TEAL = (
            0,
            128,
            128,
            255,
        )[:3]
        self.THISTLE = (
            216,
            191,
            216,
            255,
        )[:3]
        self.THISTLE1 = (
            255,
            225,
            255,
            255,
        )[:3]
        self.THISTLE2 = (
            238,
            210,
            238,
            255,
        )[:3]
        self.THISTLE3 = (
            205,
            181,
            205,
            255,
        )[:3]
        self.THISTLE4 = (
            139,
            123,
            139,
            255,
        )[:3]
        self.TOMATO = (
            255,
            99,
            71,
            255,
        )[:3]
        self.TOMATO2 = (
            238,
            92,
            66,
            255,
        )[:3]
        self.TOMATO3 = (
            205,
            79,
            57,
            255,
        )[:3]
        self.TOMATO4 = (
            139,
            54,
            38,
            255,
        )[:3]
        self.TURQUOISE = (
            64,
            224,
            208,
            255,
        )[:3]
        self.TURQUOISE1 = (
            0,
            245,
            255,
            255,
        )[:3]
        self.TURQUOISE2 = (
            0,
            229,
            238,
            255,
        )[:3]
        self.TURQUOISE3 = (
            0,
            197,
            205,
            255,
        )[:3]
        self.TURQUOISE4 = (
            0,
            134,
            139,
            255,
        )[:3]
        self.VIOLET = (
            238,
            130,
            238,
            255,
        )[:3]
        self.VIOLET_RED = (
            208,
            32,
            144,
            255,
        )[:3]
        self.VIOLET_RED1 = (
            255,
            62,
            150,
            255,
        )[:3]
        self.VIOLET_RED2 = (
            238,
            58,
            140,
            255,
        )[:3]
        self.VIOLET_RED3 = (
            205,
            50,
            120,
            255,
        )[:3]
        self.VIOLET_RED4 = (
            139,
            34,
            82,
            255,
        )[:3]
        self.WHEAT = (
            245,
            222,
            179,
            255,
        )[:3]
        self.WHEAT1 = (
            255,
            231,
            186,
            255,
        )[:3]
        self.WHEAT2 = (
            238,
            216,
            174,
            255,
        )[:3]
        self.WHEAT3 = (
            205,
            186,
            150,
            255,
        )[:3]
        self.WHEAT4 = (
            139,
            126,
            102,
            255,
        )[:3]
        self.WHITE = (
            255,
            255,
            255,
            255,
        )[:3]
        self.YELLOW = (
            255,
            255,
            0,
            255,
        )[:3]
        self.YELLOW2 = (
            238,
            238,
            0,
            255,
        )[:3]
        self.YELLOW3 = (
            205,
            205,
            0,
            255,
        )[:3]
        self.YELLOW4 = (
            139,
            139,
            0,
            255,
        )[:3]

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
