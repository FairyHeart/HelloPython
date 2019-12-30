dict = {'k1': 'value', 'k2': 2, ('a', 'b'): 'c'}  # 键必须是唯一的，但键必须是不可变的，如字符串，数字或元组。,值可以取任何数据类型
print(dict)
print(type(dict['k1']))  # 字典里面可以同时存储不同类型的值
print(type(dict['k2']))

# ---- 访问字典 ----
print(dict['k1'])
# print(dict['m'])  # 用字典里没有的键访问数据，会输出错误 KeyError: 'm'

# ---- 修改字典 ----
dict['k1'] = "hello"  # 更新
print(dict)
dict['m'] = 'python'  # 如果没有就添加信息
print(dict)

# ---- 删除元素 ----
del dict['k1']  # 删除键 'k1'
print(dict)
dict.clear()  # 清空字典
print(dict)
# del dict  # 删除字典

# ---- 函数和方法 ----
dict = {'k1': 'value', 'k2': 2, 'k3': 'c'}
print(len(dict))
print(str(dict))
dict2 = dict.copy()  # 返回一个字典的浅复制
print(id(dict), dict, id(dict2), dict2)
print('k1' in dict)  # 如果键在字典dict里返回true，否则返回false
print(dict.items())  # 以列表返回可遍历的(键, 值) 元组数组
print(dict.keys())  # key list()列表
dict.setdefault('k5', "xyz")  # 如果键不存在于字典中，将会添加键并将值设为xyz
print(dict)
dict.update({'x': 'x', 'y': 'y'})  # 把字典dict2的键/值对更新到dict里
print(dict)
print(dict.values())  # 返回字典值的list()列表
dict.pop('x')  # 删除字典给定键 key 所对应的值
print(dict)
dict.popitem()  # 随机返回并删除字典中的最后一对键和值。
print(dict)
