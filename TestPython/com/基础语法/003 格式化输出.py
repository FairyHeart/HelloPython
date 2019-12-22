# 1.占位符格式化输出

# %s
print("\n---- %s ----")
name = "guazi"
print("Name：%s" % (name))
print("Name：%s" % name)

# 指定占位符宽度，为何从6开始？
print("Name：%6s" % name)

# %d
print("\n---- %d ----")
age = 30
print("Age：%d" % age)
print("Name:%s , Age:%d" % (name, age))

# %f
print("\n---- %f ----")
a = 123.123
print("a = %f" % a)
print("a = %.2f" % a)  # 2保留的位数
print("%.2f" % 123.456)  # 保留位数之后的小数按四舍五入处理，其结果为：123.46
print("a = %.1f" % a)
print("a = %10.2f" % a)

# 指定建的方式，对应起来提供值
# print("花名：%(name)s,年龄：%(age)d" % (name, age))  # TypeError: format requires a mapping
print("Name：%(name)s,Age：%(age)d" % {"name": name, "age": age})

# 输入% 使用%%
print("%d %%" % 100)
