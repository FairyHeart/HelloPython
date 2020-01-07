# 计算1-100之和
sum = 0
num = 100
count = 1
while count <= num:
    sum += count
    count += 1
print("1到%d之和为:%d" % (num, sum))  # 1到100之和为:5050

a = 0
while a < 4:
    a += 1
    print(a)
else:
    print("a>4")

# 简单语句组:如果你的while循环体中只有一条语句，你可以将该语句与while写在同一行中
# while (True): print("always True")
print()

# for语句
languages = ['C', 'C++', 'Java', 'Python', 'Kotlin']
for x in languages:
    if x == 'Python':
        break  # break 语句用于跳出当前循环体
    elif x == 'Java':
        continue  # continue 跳过当前循环块中的剩余语句，然后继续进行下一轮循环
    print(x)
else:
    print("for end")

# range()函数
languages = ['C', 'C++', 'Java', 'Python', 'Kotlin']
for x in range(len(languages)):
    print(x, languages[x])

# pass语句
for x in 'python':
    if x == 'o':
        pass
    else:
        print(x)
