# --------迭代器-------
it2 = iter(['a', 'b', 'c'])
print(next(it2))  # 输出迭代器的下一个元素
print(next(it2))

lists = [1, 2, 3, 4, 5]
it = iter(lists)  # 创建迭代器对象
for x in it:
    print(x, end=' ')
print()


# --------创建一个迭代器--------
class MyIter:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a < 10:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myIter = MyIter()
myIt = iter(myIter)
for x in myIt:
    print(x)

print()


# -------- 生成器 --------
def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while counter <= n:
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

for x in f:
    print(x, end=" ")
