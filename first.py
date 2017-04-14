#!/usr/bin/python
# -*- coding: UTF-8 -*-
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
# 這是個單詞
word = 'world'
# 這是一個句子
sentence = "這是一個句子"
# 這是一個段落，包含了多個語句
paragraph = "這是一個段落，包含了多個語句"
if True:
    print days
    print word
    print sentence
    print paragraph
    # 三引号的使用
    print "----------------"
    a = '''
    这是多行注释，使用单引号。
    这是多行注释，使用单引号。
    这是多行注释，使用单引号。
    '''

    """
    这是多行注释，使用双引号。
    这是多行注释，使用双引号。
    这是多行注释，使用双引号。
    """
    print a;
    print "----------------"

    # 空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。
    print "空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。"
    print "----------------"
    # 等待用户输入
    "\n\n"
    # raw_input 在结果输出前会输出两个新的空行。一旦用户按下 enter(回车)键退出，其它键显示
    raw_input("hello world")
    import sys;

    x = "soyoungboy";
    sys.stdout.write(x + '')
    # print 默认输出是换行的，如果要实现不换行需要在变量末尾加上逗号
    x = "wangfubin"
    y = "liqiongqiong"
    z = " love "
    # 换行输出
    print x
    print y
    # 不换行输出
    print x,
    print z,
    print y,
