# ---- 定义 ----
lists = {'a', 'b', 'c', 'd', 'a', 'b'}
print(lists)  # 集合会自动去重
print(set("abcd"))
print(set((1, 2, 3)))
print(set([1, 3, 2]))

# ---- 操作符----
a = set('abcdef')
b = set('abcxyz')
print(a - b)  # 集合a中包含而集合b中不包含的元素
print(a | b)  # 集合a或b中包含的所有元素
print(a & b)  # 集合a和b中都包含了的元素
print(a ^ b)  # 不同时包含于a和b的元素
# print(a + b)  # TypeError: unsupported operand type(s) for +: 'set' and 'set'
print("a" in a)  # 快速判断元素是否在集合内

# 集合支持集合推导式
c = {x for x in 'abcdef' if x not in 'abc'}
print(c)

# ---- 基本操作----
x = set('ab')
x.add("1")  # 添加元素
print(x)
x.update({2, 3})  # 添加元素，且参数可以是列表，元组，字典等
print(x)
x.update([4])
print(x)

x.remove('a')  # 集合中移除，如果元素不存在，则会发生错误
# x.remove('x')  # KeyError: 'x'
print(x)
x.discard('b')
x.discard('x')
print(x)

x.pop()  # 随机删除集合中的一个元素
print(x)

x.clear()  # 清空集合
print(x)

# ---- 方法 ----
print(set('abc').difference(set('abxyz')))  # 返回多个集合的差集
print(set('abc').intersection(set('abxyz')))  # 返回集合的交集
print(set('abc').isdisjoint(set('abxyz')))  # 判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
s1 = set('abc')
s2 = set('ab')
print(s1.issubset(s2))  # 判断指定集合是否为该方法参数集合的子集。s1是否为s2的子集
print(s1.issuperset(s2))  # 判断该方法的参数集合是否为指定集合的子集，s2是否为s1的子集
print(set('abc').symmetric_difference(set('abxyz')))  # 返回两个集合中不重复的元素集合。
print(set('abc').union(set('abxyz')))  # 返回两个集合的并集
