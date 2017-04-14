#!/usr/bin/python
#coding=utf-8
from hashlib import md5
import os
import sys
import json

def generate_file_md5value(fpath):
    '''以文件路径作为参数，返回对文件md5后的值
        '''
    m = md5()
    #需要使用二进制格式读取文件内容
    a_file = open(fpath, 'rb')
    m.update(a_file.read())
    a_file.close()
    return m.hexdigest()

def get_md5_from_json(fpath):
    f = open("config.json")
    dict = json.load(f)
    f.close
    return dict["md5"]

def check_md5(fpath, md5Sring):
    md5String2 = generate_file_md5value(fpath)
    if md5Sring == md5String2:
        return 0
    else:
        return 1

print sys.argv[0]
print sys.argv[1]
print sys.argv[2]

# md5Sring = get_md5_from_json(sys.argv[2])
# result=check_md5(sys.argv[1], md5Sring)
# sys.exit(result)
