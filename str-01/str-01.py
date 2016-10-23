#!/usr/bin/env python
# coding: utf-8
from __future__ import print_function

"""
    Created by: Arthur - 黑小帅
    Created on: 2016-10-23
    str-01 逆转字符串——输入一个字符串，将其逆转并输出。[x]
"""

char = 'Arthur'

# 方法1	 python中最优, 最为推荐
_char = char[::-1]
print(_char)

# 方法2  因为python list的特性, 此方法是效率最低的.
tmp = []
for el in char:
	tmp.insert(0, el)
_char = "".join(tmp)

print(_char)

# 方法3
tmp = [i for i in char]
tmp.reverse()
_char = ''.join(tmp)

print(_char)
