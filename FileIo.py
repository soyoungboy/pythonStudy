# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
# s = raw_input("请输入内容:")
# print "输入的内容是 = " + s

# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# # 打开一个文件
# fo = open("foo.txt", "wb")  # 没有就会去创建foo.text
# fo.write("你必须先用Python内置的open()函数打开一个文件，创建一个file对象，相关的方法才可以调用它进行读写。");
#
# print "文件名: ", fo.name  # 显示文件名称
# print "是否已关闭 : ", fo.closed
# print "访问模式 : ", fo.mode
# print "末尾是否强制加空格 : ", fo.softspace
# # File 对象的 close（）方法刷新缓冲区里任何还没写入的信息，并关闭该文件，这之后便不能再进行写入。
# # 当一个文件对象的引用被重新指定给另一个文件时，Python 会关闭之前的文件。用 close（）方法关闭文件是一个很好的习惯
# fo.close();
# print "是否已关闭 : ", fo.closed

# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# # 打开一个文件
# fo = open("foo.txt", "r+")
# str = fo.read(12);
# print "读取的字符串是 : ", str
#
# # 查找当前位置
# position = fo.tell();
# print "当前文件位置 : ", position
#
# # 把指针再次重新定位到文件开头
# position = fo.seek(0, 0);
# str = fo.read(20);
# print "重新读取字符串 : ", str
# # 关闭打开的文件
# fo.close()

# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# import os
#
# # 重命名文件test1.txt到test2.txt。
# os.rename("foo.txt", "ILoveJohn.txt")

# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# import os
#
# # 删除一个已经存在的文件test2.txt
# os.remove("ILoveJohn.txt")

# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# import os
# os.mkdir("haha")
# !/usr/bin/python
# -*- coding: UTF-8 -*-
import os

getcwd = os.getcwd()
print getcwd
# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
# import os
#
# os.rmdir('haha')
