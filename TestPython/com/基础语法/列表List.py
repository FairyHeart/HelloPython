lists = ["a", "b", "c", "d", "e"]
print(lists)  # 输出完整列表
print(lists[0])  # 输出列表第一个元素
print(lists[1:3])  # 从第二个开始输出到第三个元素
print(lists[:4])  # 输出从第0个开始到第四个的元素
print(lists[3:])  # 输出从第四个元素开始的所有元素
print(lists[:])  # 输出所有元素
print(lists[:-2])  # 输出倒数第二个元素之前的元素

lists[2] = 100
lists[3:4] = ["hello", "python"]
print(lists)

del lists[0]  # 删除第一个元素
print(lists)
del lists[1:3]  # 删除第二个到第四直接的元素
print(lists)

print(len([1, 2, 3]))  # 长度
print([1, 2] + ['a', 'b'])  # 组合
print([' ha '] * 4)  # 重复
print(3 in [1, 3, 5])  # 元素是否存在于列表
for x in [1, 3, 5, 7]:  # 迭代
    print(x)
a = ['a', 'b', 'c']
b = [1, 2, 3]
c = [a, b]  # 嵌套列表
print(c)
print()

# ---- List函数、方法 ----
lists = ["a", "b", "c", "d", "e", 'b']
print(len(lists))  # 长度
print(max(lists))  # 最大值
print(min(lists))  # 最小值

tuples = ('xyz', 123)
print(tuples)
print(list(tuples))  # 元组转列表

lists.append("x")  # 添加
print(lists)
print(lists.count("b"))  # 统计
print(lists.index("b"))  # 查找

lists.insert(3, "xyz")  # 插入
print(lists)

print(lists.pop())  # 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
print(lists)

lists.remove("b")  # 移除列表中某个值的第一个匹配项
print(lists)
lists.reverse()  # 反向列表中元素
print(lists)
lists.sort()  # 对原列表进行排序
print(lists)
lists.clear()  # 清空列表
print(lists)

a = [1, 2]
b = a.copy()  # 复制的列表，对应的引用也复制了，修改值不会更改原来的列表的值
b[0] = 'a'
print(id(a), id(b), a, b)

