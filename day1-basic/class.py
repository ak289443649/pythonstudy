# class

import types

class Demo:
    # 关于类的初始化方法，init就是一个构造器
    # 在类的实例化时，会调用该构造器的__init__()方法
    # self 是每个类的this对象 , self.name = this.name
    def __init__(self,name):
        self.name = name
    def exec(self):
        print(self.name)
# 一下这步叫做创建实例
# 只有创建实例后，才会拥有访问成员变量和方法的权限
demo = Demo('test')
demo.exec()

# 这里有个非常有趣的事情
# function 和 method 的区别是，一个在类外定义，一个在类中定义
# 方法需要声明类才可以进行调用，而函数可以直接进行调用

def func(self,value):
    self.score = value

Demo = type('Demo', (object,), {'func': func,'__repr__': lambda self: f"Demo(score={getattr(self, 'score', None)})"})

demo = Demo()
demo.func(18)
print(demo)