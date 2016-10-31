# coding: utf-8
#!/usr/bin/env python

"""
    Created by: Arthur - 黑小帅
    Created on: 2016-10-23
    str-03 统计元音字母——输入一个字符串，统计处其中元音字母的数量。
    更复杂点的话统计出每个元音字母的数量。[x]
"""

#  *** 统计有元音字母数量 ***
text = 'this is a text, some vowel in this'

count_1 = 0

# 思路简单统计的统计
for ele in text:
    if ele in 'aeiou':
        count_1 += 1

print count_1

# 一行代码处理此问题
print len([ele for ele in text if ele in 'aeiou'])


#   *** 统计元音各个数量 ***
dic_tmp = {}
for ele in text:
    if ele in 'aeiou':
        if ele not in dic_tmp.values():
            dic_tmp[i] = 1
        else:
            dic_tmp[i] += 1

# 利用python的collections模块 一行代码处理此问题
from collections import Counter
print {k:v for k, v in Counter(text).items() if k in "aeiou"}
