#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 算数运算符

# +	加 - 两个对象相加
# -	减 - 得到负数或是一个数减去另一个数
# *	乘 - 两个数相乘或是返回一个被重复若干次的字符串
# /	除 - x除以y
# %	取模 - 返回除法的余数
# **	幂 - 返回x的y次幂
# //	取整除 - 返回商的整数部分
# a = 10
# b = 20
# print a + b
# print a - b
# print a * b
# print a / b
# print a % b
# print a ** b
# print a // b
# # Python比较运算符
# print "-------------------------------"
#       以下假设变量a为10，变量b为20：
# ==	等于 - 比较对象是否相等	(a == b) 返回 False。
# !=	不等于 - 比较两个对象是否不相等	(a != b) 返回 true.
# <>	不等于 - 比较两个对象是否不相等	(a <> b) 返回 true。这个运算符类似 != 。
# >     大于 - 返回x是否大于y	(a > b) 返回 False。
# <	    小于 - 返回x是否小于y。所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价。注意，这些变量名的大写。	(a < b) 返回 true。
# >=	大于等于	- 返回x是否大于等于y。	(a >= b) 返回 False。
# <=	小于等于 -	返回x是否小于等于y。	(a <= b) 返回 true。
# a = 21
# b = 10
# c = 0
#
# if ( a == b ):
#    print "1 - a 等于 b"
# else:
#    print "1 - a 不等于 b"
#
# if ( a != b ):
#    print "2 - a 不等于 b"
# else:
#    print "2 - a 等于 b"
#
# if ( a <> b ):
#    print "3 - a 不等于 b"
# else:
#    print "3 - a 等于 b"
#
# if ( a < b ):
#    print "4 - a 小于 b"
# else:
#    print "4 - a 大于等于 b"
#
# if ( a > b ):
#    print "5 - a 大于 b"
# else:
#    print "5 - a 小于等于 b"
#
# # 修改变量 a 和 b 的值
# a = 5;
# b = 20;
# if ( a <= b ):
#    print "6 - a 小于等于 b"
# else:
#    print "6 - a 大于  b"
#
# if ( b >= a ):
#    print "7 - b 大于等于 a"
# else:
#    print "7 - b 小于 a"
# a = 60  # 60 = 0011 1100
# b = 13  # 13 = 0000 1101
# c = 0
#
# c = a & b;  # 12 = 0000 1100
# print "1 - c 的值为：", c
#
# c = a | b;  # 61 = 0011 1101
# print "2 - c 的值为：", c
#
# c = a ^ b;  # 49 = 0011 0001
# print "3 - c 的值为：", c
#
# c = ~a;  # -61 = 1100 0011
# print "4 - c 的值为：", c
#
# c = a << 2;  # 240 = 1111 0000
# print "5 - c 的值为：", c
#
# c = a >> 2;  # 15 = 0000 1111
# print "6 - c 的值为：", c

# Python逻辑运算符
# Python语言支持逻辑运算符，以下假设变量 a 为 10, b为 20:
# 运算符	逻辑表达式	描述	实例
# and	x and y	布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。	(a and b) 返回 20。
# or	x or y	布尔"或"	- 如果 x 是非 0，它返回 x 的值，否则它返回 y 的计算值。	(a or b) 返回 10。
# not	not x	布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。	not(a and b) 返回 False
# !/usr/bin/python
# -*- coding: UTF-8 -*-

# a = 10
# b = 20
#
# if ( a and b ):
#    print "1 - 变量 a 和 b 都为 true"
# else:
#    print "1 - 变量 a 和 b 有一个不为 true"
#
# if ( a or b ):
#    print "2 - 变量 a 和 b 都为 true，或其中一个变量为 true"
# else:
#    print "2 - 变量 a 和 b 都不为 true"
#
# # 修改变量 a 的值
# a = 0
# if ( a and b ):
#    print "3 - 变量 a 和 b 都为 true"
# else:
#    print "3 - 变量 a 和 b 有一个不为 true"
#
# if ( a or b ):
#    print "4 - 变量 a 和 b 都为 true，或其中一个变量为 true"
# else:
#    print "4 - 变量 a 和 b 都不为 true"
#
# if not( a and b ):
#    print "5 - 变量 a 和 b 都为 false，或其中一个变量为 false"
# else:
#    print "5 - 变量 a 和 b 都为 true"
# !/usr/bin/python
# -*- coding: UTF-8 -*-
#
# a = 10
# b = 20
# list = [1, 2, 3, 4, 5 ];
#
# if ( a in list ):
#    print "1 - 变量 a 在给定的列表中 list 中"
# else:
#    print "1 - 变量 a 不在给定的列表中 list 中"
#
# if ( b not in list ):
#    print "2 - 变量 b 不在给定的列表中 list 中"
# else:
#    print "2 - 变量 b 在给定的列表中 list 中"
#
# # 修改变量 a 的值
# a = 2
# if ( a in list ):
#    print "3 - 变量 a 在给定的列表中 list 中"
# else:
#    print "3 - 变量 a 不在给定的列表中 list 中"

a = 20
b = 20

if (a is b):
    print "1 - a 和 b 有相同的标识"
else:
    print "1 - a 和 b 没有相同的标识"

if (id(a) is not id(b)):
    print "2 - a 和 b 有相同的标识"
else:
    print "2 - a 和 b 没有相同的标识"

# 修改变量 b 的值
b = 30
if (a is b):
    print "3 - a 和 b 有相同的标识"
else:
    print "3 - a 和 b 没有相同的标识"

if (a is not b):
    print "4 - a 和 b 没有相同的标识"
else:
    print "4 - a 和 b 有相同的标识"
