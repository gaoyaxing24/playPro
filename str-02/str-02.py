# coding: utf-8
#!/usr/bin/env python

"""
    Created by: Arthur - 黑小帅
    Created on: 2016-10-23
    str-02 拉丁猪文字游戏——这是一个英语语言游戏。基本规则是将一个
    英语单词的第一个辅音音素的字母移动到词尾并且加上后缀-ay
    譬如“banana”会变成“anana-bay”）。可以在维基百科上了解更多内容。[x]
"""

import re

ori = 'banana'

# 方法1
pre = ''
suf = ''

for el in range(len(ori)):
    if ori[el] not in 'aeiouAEIOU':
        pre += ori[el]
    else:
        suf = ori[el:]
        break

new = suf + '-' + pre + 'ay'

print new

# 方法2
tmp = re.findall(r'.*?[aeiouAEIOU]', ori)

if len(tmp) > 0:
    pre, pre2 = tmp[0][:-1], tmp[0][-1:]
    suf = pre2 + "".join(tmp[1:])

    new = suf + '-' + pre + 'ay'
    print new
else:
    print(u'文字不符合游戏规则')

# 方法3 只使用字符串自身方法
for i in 'aeiou':
    index = ori.lower().find(i)
    if index != -1:
        new = ori[index:] + '-' + ori[:index] + 'ay'

print new


