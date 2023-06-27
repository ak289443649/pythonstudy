# class
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