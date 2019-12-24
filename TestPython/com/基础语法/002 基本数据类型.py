# ---- 多个变量赋值 ----
a = b = c = 1  # 三个变量被赋予相同的数值
a, b, c = 1, 2, "python"  # 两个整型对象 1 和 2 的分配给变量 a 和 b，字符串对象 "python" 分配给变量

# ---- number数字 ----
a, b, c, d = 20, 3E-2, True, 4 + 3j
print(a, b, c, d)
print(type(a), type(b), type(c), type(d))
print(isinstance(a, int), isinstance(b, float), isinstance(c, bool), isinstance(d, complex))
print(a + c)
print()

del a, b
# print(a)

# ---- 数值运算 ----
print(5 + 4)
print(4.5 - 2)
print(3 * 7)
print(24 / 5)  # 除法，得到一个浮点数
print(24 // 5)  # 除法，得到一个整数
print(16 % 3)  # 取余
print(2 ** 5)  # 乘方

# ---- 字符串 ----
word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
可以由多行组成"""
print('hello \'python\'')
print(r'hello \'python\'')
print("hello" + " python")
print("hello " * 2)

str = 'hello python'
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始后的所有字符

# ---- List（列表） ----

# ---- ----
# ---- ----
# ---- ----
# ---- ----
# ---- ----
# ---- ----
