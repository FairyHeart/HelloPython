# -*- coding: UTF-8 -*- # 源码文件指定编码

# ---- Python标识符 ----
# 2.1 可以包括英文、数字以及下划线(_)，但不能以数字开头；
# 2.2 标识符区分大小写；
# 2.3 以下划线开头的标识符是有特殊意义；
# 以单下划线开头 _foo 的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用 from xxx import * 而导入。
# 以双下划线开头的 __foo 代表类的私有成员，以双下划线开头和结尾的 __foo__ 代表 Python 里特殊方法专用的标识，如 __init__() 代表类的构造函数。
# 2.4 不能使用保留的关键字命名
# 2.4 同一行显示多条语句，方法用“；”分开

# 15x = "a" #2.1 不能以数字开头
false = "a"
print(false)  # 2.2 标识符区分大小写

# ---- 关键字 ----
import keyword

print(keyword.kwlist)

# ---- 注释 ----
'''
 x = 'hello python'
'''
"""
 x = 'hello python'
"""

# ---- 行和缩进 ----
if True:
    print("Answer")
    print("True")
else:
    print("Answer")
#  print ("False")    # 缩进不一致，会导致运行错误 IndentationError: unindent does not match any outer indentation level

# ---- 多行语句 ----
item = "a" \
       "b" \
       "c"
print(item)

a = ['a', 'b',
     'c', 'd']
print(a)

# ---- 输入 ----
# a = input("请输入一个值：")
# print(type(a))

# ----  输出 ----
y = 'hello'
z = "中国"
print(y, z)
# sep = 分隔符 ,end代表结尾的字符，默认是\n
print(y, z, sep=" *** ", end='')
print()
# ---- import 与 from...import ----
import sys
from sys import argv, path

print(argv)
print(path)

# ---- ----
help(sys)

