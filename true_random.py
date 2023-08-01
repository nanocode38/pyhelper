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
"""
applied environment: Microsoft Windows 10, Python3.7+
Copyright (C)
By nanocode38 2602422835@qq.com
2023.7.18
"""
import copy
import os
import random
import struct

__all__ = [
    'randint',
    'choice',
    'randrange',
    'shuffle',
    'sample'
]

def _r():
    rs = struct.unpack('Q', os.urandom(8))[0]
    strr = str(rs)
    strr = strr[random.randint(1, 17)]
    rs = int(strr)
    return rs



def randint(min:int, max:int):
    """生成范围在[a, b]之间的随机整数"""
    if min > max:
        raise ValueError("The lower limit should be less than or equal to" + \
        " the upper limit")

    diff = max - min + 1
    rand_num = _r()
    return min + rand_num % diff

def choice(seq:list):
    seqlen = len(seq)
    if seqlen <= 0:
        raise IndexError
    return seq[randint(0, seqlen - 1)]

def randrange(start:int, stop:int=None, step:int=None):
    if stop == None:
        stop = start
        start = 1
        step = 1
    elif step == None:
        step = 1
    start = int(start)
    step = int(step)
    stop = int(stop)
    return choice(range(start, stop + 1, step))


def shuffle(seq):
    # 复制一份原序列
    shuffled = copy.deepcopy(seq)

    # 根据原序列的长度，进行随机交换操作
    for i in range(len(shuffled) - 1, 0, -1):
        j = _r() % (i + 1)
        shuffled[i], shuffled[j] = shuffled[j], shuffled[i]

    return shuffled

def sample(population, k):
    if k > len(population):
        raise ValueError("The number of samples is larger than the population!")

    sampled = []
    population_copy = copy.deepcopy(population)

    for _ in range(k):
        # 生成随机索引
        index = _r() % len(population_copy)

        # 从剩余的元素中随机选择一个，并添加到样本列表中
        sampled.append(population_copy[index])

        # 从总体中移除已经抽样的元素
        population_copy.pop(index)

    return sampled
