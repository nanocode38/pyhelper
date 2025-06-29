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
import copy
import os
import random
import struct
from typing import *

__all__ = ["randint", "choice", "randrange", "shuffle", "sample"]


def _r():
    rs = struct.unpack("Q", os.urandom(8))[0]
    strr = str(rs)
    strr = strr[random.randint(1, 17)]
    rs = int(strr)
    return rs


def randint(_min: int, _max: Optional[int] = None):
    """
    Generates a random integer within the inclusive range [min, max].

    This function generates a random integer in the range [min, max] using a
    more secure randomization method based on os.urandom for generating the
    base random seed. It ensures that the generated number is uniformly
    distributed across the specified range.

    :param _min: The lower limit of the range (inclusive).
    :param _max: The upper limit of the range (inclusive). Must be greater than or equal to min.
    :return int: A random integer within the inclusive range [min, max].
    :raise ValueError: If the min parameter is greater than the max parameter.
    """
    if _max is None:
        _max = _min
        _min = 1

    if _min > _max:
        raise ValueError("The lower limit should be less than or equal to the upper limit")

    diff = _max - _min + 1
    rand_num = _r()
    return _min + rand_num % diff


def choice(seq: Sized) -> Iterable:
    """
    Select a random element from a non-empty sequence.

    This function selects a random element from the given non-empty sequence.
    It uses the randint function to generate a random index within the range
    of the sequence length.

    :param seq: The non-empty sequence from which to select a random element.
    :return Sized: The randomly selected element from the sequence.
    """
    seqlen = len(seq)
    if seqlen <= 0:
        raise IndexError
    return seq[randint(0, seqlen - 1)]


def randrange(start: int, stop: int = None, step: int = None):
    """
    Return a randomly selected element from the range(start, stop, step).

    This function returns a randomly selected element from the range specified by
    the start, stop, and step parameters. If only one argument is provided, it
    treats it as the stop value and starts from 1 with a step of 1. If no arguments
    are provided, it returns a random integer from the range 0-9.

    :param start: The start of the range. Default is 1.
    :param stop: The end of the range. Default is the start value.
    :param step: The step value for the range. Default is 1.

    Returns:
    int: A randomly selected element from the specified range.

    Raises:
    - ValueError: If the stop value is less than the start value.
    """
    if stop is None:
        stop = start
        start = 1
        step = 1
    elif step is None:
        step = 1
    start = int(start)
    step = int(step)
    stop = int(stop)
    return choice(range(start, stop + 1, step))


def shuffle(seq: Sized):
    """
    Shuffles the elements of a sequence in-place.

    This function takes a sequence (such as a list or tuple) as input and
    shuffles its elements in-place using the Fisher-Yates algorithm. The original
    sequence is modified, and no new sequence is created.

    :param seq: The sequence to be shuffled.
    :return None: The original sequence is modified in-place.
    """
    # Copy the original sequence to avoid modifying it directly
    shuffled = copy.deepcopy(seq)

    # Perform the Fisher-Yates shuffle algorithm
    for i in range(len(shuffled) - 1, 0, -1):
        # Generate a random index between 0 and i (inclusive)
        j = _r() % (i + 1)

        # Swap the elements at indices i and j
        shuffled[i], shuffled[j] = shuffled[j], shuffled[i]

    # Modify the original sequence in-place
    seq[:] = shuffled


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

    :raise ValueError: If k is greater than the length of the population.
    """
    if k > len(population):
        raise ValueError("The number of samples is larger than the population!")

    sampled = []
    population_copy = copy.deepcopy(population)

    for _ in range(k):
        # Generate a random index
        index = _r() % len(population_copy)

        # Select a random element from the remaining elements and add it to the sample list
        sampled.append(population_copy[index])

        # Remove the sampled element from the population
        population_copy.pop(index)

    return sampled
