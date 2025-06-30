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
# nanocode24@outlook.com
# nanocode38
"""
A random function library for generating truly random numbers
Copyright (C)
"""
import os
from typing import *

__all__ = ["randint", "choice", "randrange", "shuffle", "sample"]


def random():
    # 使用 os.urandom 生成 7 个字节的随机数据
    byte_data = os.urandom(7)
    # 将字节数据转换为一个 53 位的整数
    int_data = int.from_bytes(byte_data, byteorder="big") & ((1 << 53) - 1)
    # 转换为 [0.0, 1.0) 范围内的浮点数
    return int_data / (1 << 53)


def randint(_min: int, _max: Optional[int] = None, random: Callable = random):
    """
    Generates a random integer within the inclusive range [min, max].

    This function generates a random integer in the range [min, max] using a
    more secure randomization method based on os.urandom for generating the
    base random seed. It ensures that the generated number is uniformly
    distributed across the specified range.

    :param _min: The lower limit of the range (inclusive).
    :param _max: The upper limit of the range (inclusive). Must be greater than or equal to min.
    :param random: Optional parameters for generating random dependency functions, default to random() functions generated using os.urandom()
    :return int: A random integer within the inclusive range [min, max].
    :raise ValueError: If the min parameter is greater than the max parameter.
    """
    if _max is None:
        _max = _min
        _min = 1

    if _min > _max:
        raise ValueError("The lower limit should be less than or equal to the upper limit")

    return int(random() * (_min - _max + 1)) + _max


def choice(seq: Sequence, random: Callable = random) -> Iterable:
    """
    Select a random element from a non-empty sequence.

    This function selects a random element from the given non-empty sequence.
    It uses the randint function to generate a random index within the range
    of the sequence length.

    :param seq: The non-empty sequence from which to select a random element.
    :param random: Optional parameters for generating random dependency functions, default to random() functions generated using os.urandom()
    :return Sized: The randomly selected element from the sequence.
    :raise IndexError: When the sequence provided is empty
    """
    if len(seq) <= 0:
        raise IndexError("Cannot choose from an empty sequence")
    return seq[int(random() * len(seq))]


def randrange(start: int, stop: int = None, step: int = 1, random: Callable = random):
    """
    Return a randomly selected element from the range(start, stop, step).

    This function returns a randomly selected element from the range specified by
    the start, stop, and step parameters. If only one argument is provided, it
    treats it as the stop value and starts from 1 with a step of 1. If no arguments
    are provided, it returns a random integer from the range 0-9.

    :param start: The start of the range. Default is 1.
    :param stop: The end of the range. Default is the start value.
    :param step: The step value for the range. Default is 1.
    :param random: Optional parameters for generating random dependency functions, default to random() functions generated using os.urandom()

    :return int: A randomly selected element from the specified range.
    :raise ValueError: If the range is empty or step is zero
    :raise ValueError: If the stop value is less than the start value.
    """
    if stop is None:
        stop, start, step = start, 1, 1
    elif step == 0:
        raise ValueError("Step cannot be zero")
    if stop < start:
        raise ValueError("Stop value cannot be less than start value")
    start = int(start)
    step = int(step)
    stop = int(stop)
    return choice(range(start, stop + 1, step))


def shuffle(seq: Sequence):
    """
    Shuffles the elements of a sequence in-place.

    This function takes a sequence (such as a list or tuple) as input and
    shuffles its elements in-place using the Fisher-Yates algorithm. The original
    sequence is modified, and no new sequence is created.

    :param seq: The sequence to be shuffled.
    :return None: The original sequence is modified in-place.
    """
    # Copy the original sequence to avoid modifying it directly
    for i in reversed(range(1, len(seq))):
        j = int(random() * (i + 1))
        seq[i], seq[j] = seq[j], seq[i]


def sample(population, k) -> list:
    """
    Randomly selects k unique elements from a population sequence.

    This function takes a population sequence (such as a list or tuple) and a
    number k as input, and returns a new list containing k unique elements chosen
    randomly from the population. The original population sequence is not modified.


    :param population: The sequence from which to select elements.
    :param k: The number of elements to select. Must be less than or equal to the
             length of the population.

    :return list: A new list containing k unique elements randomly selected from the population.

    :raise TypeError: If population is not a Sequence
    :raise ValueError: If k is greater than the length of the population.
    """
    if not isinstance(population, Sequence):
        raise TypeError("Population must be a sequence")

    n = len(population)
    if k > n:
        raise ValueError("Sample size larger than population")

    result = []
    pool = list(population)
    for i in range(k):
        j = int(random() * (n - i))
        result.append(pool[j])
        pool[j] = pool[n - i - 1]
    return result
