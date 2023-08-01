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
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# DON'T EVEN HAVE A PERMIT TOO!
#
# Gao Yuhan(高宇涵)
# 2602422835@qq.com
# nanocode38

import time
from typing import *

__all__ = [
    'Timer',
    'CountUpTimer',
    'CountDownTimer',
]




class Timer:
    """A class to manage a timer with the option to execute a command after the timer finishes.
    :param time_in_seconds (float): The time in seconds the timer should run for. default: -1, It's infinite
    :param command (function): The command to execute after the timer finishes. default: None



    Attributes:
        time_in_seconds (float): The time in seconds the timer should run for.
        is_running (bool)(read only): Whether the timer is running or not.
        start_time (float)(read only): The time in seconds the timer started.
    """

    __slots__ = ['time_in_seconds', '_saved_time', '__command',
                 '__is_running', '__start_time']

    def __init__(self, time_in_seconds :float=-1, command=None):
        self.time_in_seconds = time_in_seconds
        self._saved_time = 0.0
        self.__command = command
        self.__is_running = False
        self.__start_time = 0.0

    @property
    def start_time(self):
        return self.__start_time

    @property
    def is_running(self):
        return self.__is_running

    def start(self, new_time_in_seconds=-1):
        """Start the timer with the option to change the time in seconds."""

        if new_time_in_seconds != -1:
            self.time_in_seconds = new_time_in_seconds
        self.__is_running = True
        self.__start_time = time.time()

    def update(self):
        """Update the timer's saved time."""

        if not self.__is_running:
            return
        self._saved_time = time.time() - self.__start_time
        if self._saved_time < self.time_in_seconds or self.time_in_seconds < 0:
            return

        # timer has finished
        self.stop()

    def pause(self):
        """Pause the timer."""

        self.__is_running = False

    def go_on(self):
        """Resume the timer."""

        self.__is_running = True
        self.update()

    def get_time(self):
        """Get the timer's saved time, updating it if the timer is running."""

        if self.__is_running:
            self._saved_time = time.time() - self.__start_time

        return self._saved_time

    def stop(self):
        """Stop the timer and execute the command if provided."""

        self.get_time()  # Remembers final self._saved_time
        self.__is_running = False
        if self.__command is not None:
            self.__command()
        return self.get_time()


class CountUpTimer:
    """A class to create a count-up timer that can be paused and resumed.

    This class is a subclass of the Timer class.

    Attributes:
        is_running: A boolean indicating whether the timer is running.
        saved_time: The time the timer was paused at.
        is_pause: A boolean indicating whether the timer is paused."""

    __slots__ = ['__is_running', '__saved_time', '__start_time', 'is_pause']

    def __init__(self):
        self.__is_running = False
        self.__saved_time = 0.0
        self.__start_time = 0.0  # safeguard
        self.is_pause = False

    @property
    def is_running(self):
        """Return True if the timer is running, False otherwise."""
        return self.__is_running

    @property
    def start_time(self):
        """Return the start time of the timer."""
        return self.__start_time

    def start(self):
        """Start the timer."""
        if self.is_pause:
            self.__start_time = time.time()
            # get the cutter seconds and save the value
            self.__saved_time = 0.0
        self.__is_running = True
        self.is_pause = True

    def _get_time(self):
        """Return the current time of the timer.
        This is an internal private method. If you are reading this document, you are a bad client programmer!!"""
        if not self.__is_running:
            return self.__saved_time

        self.__saved_time = time.time() - self.__start_time
        return self.__saved_time

    def get_time(self, mode='seconds'):
        """Return the current time of the timer in the specified format.


        :param mode (str): The format of the time to be returned. If 'seconds', return the time in seconds. If
        'HHMMSS',
        return the time as HH:MM:SS.

        Returns:
            If the mode is 'HHMMSS': str: The current time of the timer in the specified format.
            Else: float: The current time of the timer in seconds.
        """
        if mode != 'HHMMSS':
            return self._get_time()
        seconds = self._get_time()
        min, sec = divmod(seconds, 60)
        hours, min = divmod(int(min), 60)
        strmin = str(min)
        strhours = str(hours)
        strsec = str(sec)
        if min < 10:
            strmin = '0' + strmin
        if hours < 10:
            strhours = '0' + strhours
        if sec < 10:
            strsec = '0' + strsec
        strsec = strsec[:6]
        return f'{strhours}:{strmin}:{strsec}'

    def stop(self):
        """Stop the timer."""
        self.get_time()  # remembers final self._saved_time
        self.__is_running = False


class CountDownTimer:
    """A class to create a count-up timer that can be paused and resumed.

    This class is a subclass of the Timer class.
    """
    __slots__ = ['seconds', 'timer']
    def __init__(self, str_start_time:str, command=None):
        list_time = str_start_time.split(':')
        hours = int(list_time[0])
        min = int(list_time[1])
        sec = float(list_time[2])
        self.seconds = hours * 3600 + min * 60 + sec
        if command is not None:
            self.timer = Timer(self.seconds, command)
        else:
            self.timer = Timer(self.seconds)


    def start(self):
        """Start the timer."""
        self.timer.start()

    def update(self):
        """Update the timer."""
        self.timer.update()

    def pause(self):
        """Pause the timer."""
        self.timer.pause()

    def go_on(self):
        """Resume the timer."""
        self.timer.go_on()
        self.update()

    def get_time(self, mode='seconds'):
        """Get this Time"""
        saved_time = self.seconds - self.timer._saved_time
        if mode != 'HHMMSS':
            return saved_time
        min, sec = divmod(saved_time, 60)
        hours, min = divmod(int(min), 60)
        strmin = str(min)
        strhours = str(hours)
        strsec = str(sec)
        if min < 10:
            strmin = '0' + strmin
        if hours < 10:
            strhours = '0' + strhours
        if sec < 10:
            strsec = '0' + strsec
        strsec = strsec[:6]
        return f'{strhours}:{strmin}:{strsec}'

    def stop(self):
        """Stop the Timer"""
        self.timer.stop()