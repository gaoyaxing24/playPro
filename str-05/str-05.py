# coding: utf-8
#!/usr/bin/env python

"""
    Created by: Arthur - 黑小帅
    Created on: 2016-11-015
    str-05 统计字符串中的单词数目——统计字符串中单词的数目，
    更复杂的话从一个文本中读出字符串并生成单词数目统计结果。[x]
"""
from collections import Counter

word = 'This is python hello world.'
# 解法 以空格分割统计词数和每个单词数
new_word = word.split()

count = len(new_word)
word_count = Counter(new_word)

print "一共有: %d个单词, 每个单词出现了%s次" % (count, word_count)

# 但是不是所有的句子都是以空格隔开的   以下是引用this模块出现的结果
word = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
new_word = word.split()     # 此种方法将两面失误 1.不是所有的单词都有效识别 2.若符号中间无空格将无法获取单词

count = len(new_word)
word_count = Counter(new_word)

print "一共有: %d个单词, 每个单词出现了%s次" % (count, word_count)    # 看结果

# 此时要讲明两个概念: 
# 1.字符串是一种特殊的List, 所以才能以下标方式去访问
# 2.字符串不可更改, 日常使用的字符串修改是内部操作先开辟新内存,
# 按规则创建新字符串, 把索引放过去, 再删除原有对象.
# 例: 
# x = 'abc'   
# x = '123' 此时操作成功,   x 并不是原有内存地址, 而是开辟新内存引用过来
# x[1] (结果为2, 大家都知道) 而使用修改 x[1] = 'b'
# 此时报错 TypeError: 'str' object does not support item assignment

import string
letters = string.letters + string.whitespace    # 去掉里面的数字和特殊符号, 只留下英文字母的空符
new_word = "".join([i for i in word if i in letters]).split()

count = len(new_word)
word_count = Counter(new_word)

print "一共有: %d个单词, 每个单词出现了%s次" % (count, word_count)    # 看结果 此时结果不再有"符号单词"

# 返回头讲一讲为什么要说明上面的概念
# 有些不理解同学会这样去处理str
arthur = "Mr.Athur"
for k, v in enumerate(arthur):
    if v == '.':
        try:
            arthur[k] = ' '
        except TypeError, e:
            print "this error is %s" % e

# 这样处理看似可以节省内存空间并节省代码, 但实际是不可行的
