# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# import support
#
# support.print_func("testModule")

# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# Money = 4546
#
#
# def AddMoney():
#     # 想改正代码就取消以下注释:
#     global Money
#     Money = Money * 10+Money
#
#
# print Money
# AddMoney()
# print Money

# !/usr/bin/python
# -*- coding: UTF-8 -*-
import package_test
from package_test.support import print_func

content = dir(package_test.support)
print_func("world,I Love John");

print content;
