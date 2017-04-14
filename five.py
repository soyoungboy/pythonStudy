#!/usr/bin/python
# -*- coding: UTF-8 -*-
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [6, 7, 8, 9, 10, 1, 2, 3, 4, 5]
c = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
print "-----------列表函数和方法-------------"
print cmp(a, b)  # 比较列个列表元素
print len(b)  # b元素列表长度
print max(b)  # 显示b中最大值
print min(b)  # 显示b中最小值
print list(c)  # 元祖转化为列表
a.append(12)  # 列表末尾添加新元素,不要直接print a.append(12)
print  a
print a.count(1)  # 统计某个元素在列表中出现的次数
a.extend(b)  # 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
print a
print a.index(6)  # 从列表中找出某个值(6)第一个匹配项的索引位置
a.insert(5, 'insert here')  # 将对象插入列表
print a
b = [6, 7, 8, 9, 10, 1, 2, 3, 4, 5]
b.pop(9)  # 移除第9个元素
print b
b = [6, 7, 8, 9, 10, 1, 2, 3, 4, 5]
b.remove(10)  # 删除元素10
print b
b = [6, 7, 8, 9, 10, 1, 2, 3, 4, 5]
b.reverse()  # 列表元素翻转
print b
b = [6, 7, 8, 9, 10, 1, 2, 3, 4, 5]
b.sort()  # 对原列表进行排序
print b
