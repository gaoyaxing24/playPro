#!/usr/bin/env python
# coding: utf-8
from __future__ import print_function

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
