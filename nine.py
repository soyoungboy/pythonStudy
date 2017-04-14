# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# # 定义函数
# def printMe(str):
#     "打印任何传入的字符串"
#     print str;
#     return;
#
#
# # 调用函数
# printMe("我要调用用户自定义函数!");
# printMe("再次调用同一函数");

# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# def ChangeInt(a):
#     a = 10
#
#
# b = 2
# ChangeInt(b)
# print b  # 结果是 2

# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# # 可写函数说明
# def changeme(mylist):
#     "修改传入的列表"
#     mylist.append([1, 2, 3, 4]);
#     print "函数内取值: ", mylist
#     return
#
#
# # 调用changeme函数
# mylist = [10, 20, 30];
# changeme(mylist);
# print "函数外取值: ", mylist

# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# # 可写函数说明
# def printme(str, name, age):
#     "打印任何传入的字符串"
#     print str;
#     print name;
#     print age;
#     return;
#
#
# # 调用printme函数
# printme(str='嘻嘻哈哈', name="老王", age=27);

# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# # 可写函数说明
# def printinfo(arg1, *vartuple):
#     "打印任何传入的参数"
#     print "输出: "
#     print arg1
#     for var in vartuple:
#         print var
#     return;
#
#
# # 调用printinfo 函数
# printinfo(10);
# printinfo(50,70, 60,100,2000 );

# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# # 可写函数说明
# sum = lambda arg1, arg2: arg1 + arg2 + arg1 * arg2;
#
# # 调用sum函数
# print "相加后的值为 : ", sum(10, 20)
# print "相加后的值为 : ", sum(20, 20)

# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# # 可写函数说明
# def sum(arg1, arg2):
#     # 返回2个参数的和."
#     total = arg1 + arg2 + arg1 * arg2
#     print "函数内 : ", total
#     return total;
#
#
# # 调用sum函数
# total = sum(10, 20);
# print "函数外 : ", total

# !/usr/bin/python
# -*- coding: UTF-8 -*-

total = 0;  # 这是一个全局变量

# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2 + arg1 * arg2;  # total在这里是局部变量.
    print "函数内是局部变量 : ", total
    return total;


# 调用sum函数
sum(10, 20);
print "函数外是全局变量 : ", total