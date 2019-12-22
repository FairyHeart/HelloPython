# 变量的声明：python中变量的类型是根据赋值给它的类型来决定的，不需要声明变量的类型，不能像java语言一样声明null值
# 变量的命名规则
#   1、一般是英文单词组成，全部小写，如果两个单词以上，以下划线来进行分割
#   2、第一个字母必须是字母或者下划线，不能以数字开头，变量中不能包含空格、特殊字符
#   3、变量名对大小写敏感对
#   4、变量名不要使用python保留关键字，也不要使用内置的方法名
#   python保留关键字：
#  【Flase、None、True、and、as、assert、break、class、continue、def、del、elif、else、except、finally、for、from,
#  global、if、import、in、is、lambda、nonlocal、not、or、pass、raise、return、try、while、whith、yield】

print(type("a"),type(1),type(1.0),type(False))

false = "a"
print(false)
