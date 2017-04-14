# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# try:
#     fh = open("testfile", "w")
#     try:
#         fh.write("这是一个测试文件，用于测试异常!!")
#     finally:
#         print "关闭文件"
#         fh.close()
# except IOError:
#     print "Error: 没有找到文件或读取文件失败"


# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
# # 定义函数
# def temp_convert(var):
#     try:
#         return int(var)
#     except ValueError, Argument:
#         print "参数没有包含数字\n", Argument
#
#
# # 调用函数
# temp_convert("xyz");

# !/usr/bin/python
# -*- coding: UTF-8 -*-

# 定义函数
def mye(level):
    if level < 1:
        raise Exception("Invalid level!", level)  # 触发异常后，后面的代码就不会再执行
try:
    mye(0)  # 触发异常 level = 0 因为小于0 ，上面出发了异常
except "Invalid level!":
    print 1
else:
    print 2
