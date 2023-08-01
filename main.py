import os
import sys


__all__ = [
    'RGBColor',
    'CSSColor',
]

_PYTHON_PATH = sys.executable[:-11]
if os.name == 'nt' and _PYTHON_PATH[-6:] == 'Script':
    _PYTHON_PATH = _PYTHON_PATH[:-7]
elif os.name == 'posix' and _PYTHON_PATH[-3:] == 'bin':
    _PYTHON_PATH = _PYTHON_PATH[:-4]
_PYTHON_PATH = os.path.join(_PYTHON_PATH, 'Lib', 'site-packages', 'pyhelper')





class RGBColor:
    """
    A class about RGB colors
    The class has:
    Red
    LineGreen
    Green
    Blue
    White
    Black
    Gray
    Yellow
    Orange
    Purple
    Pink
    and
    Back(230, 230, 230)

    Examples:
    ---------
    >>> c = RGBColor.Red
    >>> c
    (255, 0, 0)
    >>> c = RGBColor.Blue
    >>> c
    (0, 0, 255)
    """
    Red = (255, 0, 0)
    LineGreen = (0, 255, 0)
    Green = (0, 128, 0)
    Blue = (0, 0, 255)
    White = (255, 255, 255)
    DarkGray = (64, 64, 64)
    Black = (000, 000, 000)
    Gray = (128, 128, 128)
    DownGray = (140, 140, 140)
    NormalGray = (170, 170, 170)
    OverGray = (210, 210, 210)
    DisabledGray = (220, 220, 220)
    Yellow = (255, 255, 000)
    Orange = (255, 165, 000)
    Purple = (128, 000, 128)
    Pink = (255, 192, 203)
    Back = (230, 230, 230)



class CSSColor:
    """
    A class about RGB colors
    The class has:
    Red
    LineGreen
    Green
    Blue
    White
    Black
    Gray
    Yellow
    Orange
    Purple
    Pink
    and
    Back(230, 230, 230)

    Examples:
    ---------
    >>> c = CSSColor.Red
    >>> c
    (255, 0, 0)
    >>> c = CSSColor.Blue
    >>> c
    (0, 0, 255)
    """
    Red = '#FF0000'
    LineGreen = '#00FF00'
    Green = '#008000'
    Blue = '#0000FF'
    White = '#FFFFFF'
    DarkGray = '#404040'
    Black = '#000000'
    Gray = '#808080'
    DownGray = '#8C8C8C'
    NormalGray = '#AAAAAA'
    OverGray = '#D2D2D2'
    DisabledGray = '#DCDCDC'
    Yellow = '#FFFF00'
    Orange = '#FFA500'
    Purple = '#800080'
    Pink = '#FFC0CB'
    Back = '#E6E6E6'