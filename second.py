#!/usr/bin/python
# -*- coding: UTF-8 -*-
# python变量类型学习
# Python 中的变量赋值不需要类型声明。
# 每个变量在内存中创建，都包括变量的标识，名称和数据这些信息。
# 每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
# 等号（=）用来给变量赋值。
# 等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值
counter = 100
miles = 1000.11
name = "john"
# Python允许你同时为多个变量赋值
a = b = c = 12345
print counter
print miles
print name
print a
print b
print c
# 标准数据类型
# Python有五个标准的数据类型：
# Numbers（数字）
# String（字符串）
# List（列表）
# Tuple（元组）
# Dictionary（字典）

# Numbers（数字）
# Python支持四种不同的数字类型：
# int（有符号整型）
# long（长整型[也可以代表八进制和十六进制]）
# float（浮点型）
# complex（复数）
print "------------------";
str = 'I love John'

print str  # 输出完整字符串
print str[0]  # 输出字符串中的第一个字符
print str[2:5]  # 输出字符串中第三个至第五个之间的字符串
print str[2:]  # 输出从第三个字符开始的字符串
print str * 2  # 输出字符串两次
print str + "TEST"  # 输出连接的字符串

# Python列表
list = [12345, 'xixihaha', 2.33, 4.56];
list2 = ['I', 7788];
print list;
print list2;
print list[0];
print list[1:3];
print list[2:];
print list2 * 2;
print list + list2;
# Python 字典
# 字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象结合，字典是无序的对象集合。
# 两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
# 字典用"{ }"标识。字典由索引(key)和它对应的值value组成。
dict = {}
dict['one'] = "haha"
dict[2] = "this is two"
print dict['one']
print dict
# Python数据类型转换
# 有时候，我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可。
# 以下几个内置的函数可以执行数据类型之间的转换。这些函数返回一个新的对象，表示转换的值。
x = 10.5
y = 10
# print int(x)  # 将x转换为一个整数
# print long(x)  # 将x转换为一个长整数
# print float(x)  # 将x转换到一个浮点数
# print complex(x)  # 创建一个复数
# print repr(x)  # 将对象 x 转换为表达式字符串
# print tuple(x)  # 将序列 s 转换为一个元组
# print list(x)
# print set(x)
# print dict(x)
# print chr(x)
print ord(z)
print hex(y)
print oct(y)