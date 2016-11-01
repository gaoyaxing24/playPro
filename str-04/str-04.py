# coding: utf-8
#!/usr/bin/env python

"""
    Created by: Arthur - 黑小帅
    Created on: 2016-11-01
    str-04 判断是否为回文——判断用户输入的字符串是否为回文。
    回文是指正反拼写形式都是一样的词，譬如“racecar”。[x]
"""

old = 'racecar'

# 简单解法
new = old[::-1]
if new == old:
	print "old=%s 它是回文, 它的回文是 %s" % (old, new)
else:
	print "old=%s不是一个回文" % old

# 中间数解法
div, _ = divmod(len(old), 2)
pre, suff = old[:div], old[-div:][::-1]

if pre == suff:
	print "old=%s 它是回文字符串" % (old, )
else:
	print "old=%s不是一个回文" % old

# 递归解法  如果递归结果为1表示此为一个回文,  若为0表示不是回文
def palindrome(palind):
	if len(palind) in [0, 1]:
		return 1
	if palind[0] != palind[-1]:
		return 0
	return palindrome(palind[1:-1])

if palindrome(old):
	print "old=%s 它是回文字符串" % (old, )
else:
	print "old=%s不是一个回文" % old

