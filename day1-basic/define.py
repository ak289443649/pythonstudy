# def
def demo(str):
    print(str)

demo('test')

def compare(str1, str2):
    if str1 == str2:
        return True
    else:
        return False

print(compare('test', 'test'))

def max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
    
print(max(3, 2))
# ** 代表该函数的关键字类型是一个dict - 包含key & value
def dictDemo(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key, value)

dictDemo(name='test', age=18)
print("==================")
# * 代表该函数的关键字类型是一个tuple - 接收即不可变
def tupleDemo(*args):
    print(type(args))
    for item in args:
        print(item)

tupleDemo(1, 2, 3, 4, 5)
print("==================")
# 给参数赋予默认值的方式是一种兜底方案
def defaultDemo(args = None):
    if args is None:
        print("default")
        args = []
    for item in args:
        print(item)

defaultDemo()

print("==================")
# lambda函数在python中是一种匿名函数，意在隐藏def关键字
pri = lambda x: print(x)
pri('test')

# / 之前的不允许加参数关键字 
# # 之后的不允许不加关键字
def f(a, b, /, *, d, e):
    print(a, b, d, e)

f(1, 2, d=3, e=4)