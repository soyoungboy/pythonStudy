# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
# # Python程序语言指定任何非0和非空（null）值为true，0 或者 null为false。
# flag = False
# name = 'luren'
# if name == 'python':  # 判断变量否为'python'
#     flag = True  # 条件成立时设置标志为真
#     print 'welcome boss'  # 并输出欢迎信息
# else:
#     print name  # 条件不成立时输出变量名称

# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
# # 例2：elif用法
#
# num = 5
# if num == 3:  # 判断num的值
#     print 'boss'
# elif num == 2:
#     print 'user'
# elif num == 1:
#     print 'worker'
# elif num < 0:  # 值小于零时输出
#     print 'error'
# elif num == 4:
#     print "right"
# else:
#     print 'roadman'  # 条件均不成立时输出

# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# # 例3：if语句多个条件
#
# num = 9
# if num >= 0 and num <= 10:    # 判断值是否在0~10之间
#     print 'hello'
#
# num = 10
# if num < 0 or num > 10:    # 判断值是否在小于0或大于10
#     print 'hello'
# else:
# 	print 'undefine'
#
# num = 8
# # 判断值是否在0~5或者10~15之间
# if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):
#     print 'hello'
# else:
#     print 'undefine'

# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# var = 100
#
# if (var == 100): print "变量 var 的值为100"
#
# print "Good bye!"

# #!/usr/bin/python
#
# count = 0
# while (count < 9):
#    print 'The count is:', count
#    count = count + 1
#
# print "Good bye!"

# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
# i = 1
# while i < 10:
#     i += 1
#     if i % 2 > 0:  # 非双数时跳过输出
#         continue
#     print i  # 输出双数2、4、6、8、10
# print "----------------------------------"
# i = 1
# while 1:  # 循环条件为1必定成立
#     print i  # 输出1~10
#     i += 1
#     if i > 10:  # 当i大于10时跳出循环
#         break
#
# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# var = 1
# while var == 1 :  # 该条件永远为true，循环将无限执行下去
#    num = raw_input("Enter a number  :")
#    print "You entered: ", num
#
# print "Good bye!"

# #!/usr/bin/python
#
# count = 0
# while count < 5:
#    print count, " is  less than 5"
#    count = count + 1
# else:
#    print count, " is not less than 5"

# #!/usr/bin/python
#
# flag = 1
#
# while (flag): print 'Given flag is really true!'
#
# print "Good bye!"

# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# for letter in 'Python':  # 第一个实例
#     print '当前字母 :', letter
#
# fruits = ['banana', 'apple', 'mango']
# for fruit in fruits:  # 第二个实例
#     print '当前水果 :', fruit
#
# print "Good bye!"

# 通过序列索引迭代
# 内置函数 len() 和 range(),函数 len() 返回列表的长度，即元素的个数。 range返回一个序列的数
# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# fruits = ['banana', 'apple', 'mango']
# i = len(fruits)
# l = range(i)
# # i相当于size,l相当于position
# print i
# print l
# for index in l:
#     print '当前水果 :', fruits[index]
#
# print "Good bye!"
# 循环使用 else 语句
# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# for num in range(10, 20):  # 迭代 10 到 20 之间的数字
#     for i in range(2, num):  # 根据因子迭代
#         if num % i == 0:  # 确定第一个因子
#             j = num / i  # 计算第二个因子
#             print '%d 等于 %d * %d' % (num, i, j)
#             break  # 跳出当前循环
#     else:  # 循环的 else 部分
#         print num, '是一个质数'

# !/usr/bin/python
# -*- coding: UTF-8 -*-
#
# i = 2
# while (i < 100):
#     j = 2
#     while (j <= (i / j)):
#         if not (i % j): break
#         j = j + 1
#     if (j > i / j): print i, " 是素数"
#     i = i + 1
#
# print "Good bye!"

# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
# for letter in 'hello world':  # First Example
#     if letter == 'o':
#         pass
#         print "-----------我是分割线-----------"
#     print 'Current Letter :', letter

# # !/usr/bin/python
#
# var1 = 'Hello World!'
# var2 = "Python Runoob"
#
# print "var1[0]: ", var1[0]  # 字符中第一个内容
# print "var2[1:5]: ", var2[1:5]  # 从位置1到位置5之间的字符

# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# var1 = 'Hello World!'
#
# print "更新字符串 :- ", var1[:6] + 'John! I Love You'  # 替换第六个位置以后的内容

# # !/usr/bin/python
#
# print "My name is %s and weight is %d kg!" % ('soyoungboy', 75)

# # !/usr/bin/python
# hi = '''hi
# there'''
# hi
# print hi
# !/usr/bin/python
hi = u'Hello\u0020World ！'
print hi
