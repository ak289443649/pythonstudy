# 装饰器模式
def decorator(func):
    def wrapper(*args, **kwargs):
        print('before func')
        func(*args, **kwargs)
        print('after func')
    return wrapper

@decorator
def func():
    print('func')

func()

# 装饰器模式返回的是一个将原有函数包装好的函数
# 该函数已经被增强过了，因此在装饰器模式内部函数中，返回一个函数本身 