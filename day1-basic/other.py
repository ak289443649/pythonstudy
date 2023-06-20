# 同一行使用多条语句使用分号；隔开
import sys; x = 'runoob'; sys.stdout.write(x + '\n')

# 不换行的print需要加end=""
print("test",end="")
print("test2",end="")
print("================================")

# from import 特定的成员
from math import *
print(pi)
print(sin(pi))
print(cos(pi))
print(tan(pi))

print("================================")
# import 整个模块
import math
print(math.pi)
print(math.sin(math.pi))
print(math.cos(math.pi))