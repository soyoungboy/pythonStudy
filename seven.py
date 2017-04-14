#!/usr/bin/python
# coding=utf-8

dict = {'Name': 'soyoungboy', 'Age': 27, 'School': 'Xian University of Finance and Economics'};
print dict.copy();  # 返回一个字典的浅复制
fromkeys = dict.fromkeys(dict)  # 创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值
print fromkeys;
dict_fromkeys = dict.fromkeys(dict, 'I Love John')  # 创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值
print dict_fromkeys;
dict = {'Name': 'soyoungboy', 'Age': 27, 'School': 'Xian University of Finance and Economics'};
print dict.get('Name', 'defaultValue');  # 返回指定键的值，如果值不在字典中返回default值,其实就是根据键获取值
print dict.get('name', 'defaultValue');
print dict.items();  # 以列表返回可遍历的(键, 值) 元组数组
print dict.keys();  # 以列表返回一个字典所有的键
dict.setdefault('Height', 'defaultValue');  # 和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
print dict;
dict = {'Name': 'soyoungboy', 'Age': 27, 'School': 'Xian University of Finance and Economics'};
dict2 = {'Name': 'john', 'Age': 27, 'School': 'South China Agricultural University'};
dict.update(dict2);  # 把字典dict2的键/值对更新到dict里
print dict;
print dict.values();  # 以列表返回字典中的所有值
