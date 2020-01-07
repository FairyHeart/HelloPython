def funTest(param1, param2):
    param1 += 1
    param2 += 2
    return param1 * param2


print(funTest(1, 1))  # 6


# --------传不可变对象实例--------
def ChangeInt(a):
    a = 10


# 实例中有 int 对象 2，指向它的变量是 b，在传递给 ChangeInt 函数时，按传值的方式复制了变量 b，a 和 b 都指向了同一个 Int 对象，在 a=10 时，则新生成一个 int 值对象 10，并让 a 指向它
b = 2
ChangeInt(b)
print(b)  # 结果是 2


# --------传可变对象实例--------
def changeme(mylist):
    mylist.append([1, 2, 3, 4])
    print("函数内取值: ", mylist)  # 函数内取值:  [10, 20, 30, [1, 2, 3, 4]]
    return


# 调用changeme函数
mylist = [10, 20, 30]
changeme(mylist)
print("函数外取值: ", mylist)  # 函数外取值:  [10, 20, 30, [1, 2, 3, 4]]

# --------参数--------
print('\n--------参数--------')


def printInfo(name, age=10):
    print("name=", name, "age=", age)


printInfo('guazi', 18)  # 必需参数
printInfo(age=18, name='guazi')  # 关键字参数
printInfo('guazi')  # age 默认参数


# 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数
def printInfo1(arg1, *vartuple):
    print(arg1, vartuple)


def printInfo12(arg1, *, arg2):
    print(arg1, arg2)


# 加了两个星号 ** 的参数会以字典的形式导入
def printInfo2(arg1, **vardict):
    print(arg1, vardict)


printInfo1('hello', 'python', 'java')
printInfo12('hello', arg2='java')  # 如果单独出现星号 * 后的参数必须用关键字传入
printInfo2('hello', a='python', b='java')

print("\n--------匿名函数--------")
sum = lambda arg1, arg2: arg1 + arg2
print(sum(1, 2))


# 强制位置参数
def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)


f(1, 2, 3, d=4, e=5, f=6)
# f(10, b=20, c=30, d=40, e=50, f=60)  # b 不能使用关键字参数的形式
# f(10, 20, 30, 40, 50, f=60)  # e 必须使用关键字参数的形式
