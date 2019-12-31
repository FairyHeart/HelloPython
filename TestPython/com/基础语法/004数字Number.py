# ---- number数字 ----
import random

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
print(24 // 5.0)  # 除法，得到不一定是一个整数，取决于分子分母
print(24.0 // 5)
print(16 % 3)  # 取余
print(2 ** 5)  # 乘方

print()

print(random.choice(range(10)))  # 从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数
print(random.randrange(3, 10, 2))  # 从指定范围内，按指定基数递增的集合中获取一个随机数，基数默认值为 1
print(random.random())  # 随机生成下一个实数，它在[0,1)范围内
print(random.uniform(1, 10))  # 随机生成下一个实数，它在[x,y]范围内
