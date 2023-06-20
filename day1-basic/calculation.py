# 数值计算

import math


num = 1
num2 = 2
# 向下取整
result = num // num2
# //并不一定返回整数类型的数据，取决于分子分母的类型
print(result)
# ** 代表乘方 num的num2次方
result = num ** num2
print(result)

num3 = -3
num3 = abs(num3)
print(num3)

print("====================")
# 赋值运算符
num = 1
num2 = 2
num += num2
# 等同于 num = num + num2
print(num)
num -= num2
# num = num - num2
print(num)

# 海象运算符 := python 3.8 VERSION
# 作用是将一个表达式的值赋值给一个变量，不需要重复循环赋值
def add(num1, num2):
    return num1 + num2

addNum1 = 1
addNum2 = 2
if (n:= add(addNum1, addNum2)) > 0:
    print(True)
else:
    print(False)

print("====================")
# 按位异或计算 
# 不同的位才为1 相同为0

# and or not
# and 比较，前值如果是False会返回前者，否则返回后者
andFlag = False
orFlag = True
if (andFlag and orFlag):
    print(True)
else:
    print(False)
print("====================")
if not (andFlag and orFlag):
    print(True)
else:
    print(False)
print("====================")
if (andFlag or orFlag):
    print(True)
else:
    print(False)
print("====================")
andNum = 10
orNum = 20
if (andNum and orNum):
    print(andNum)
else:
    print(orNum)
print("====================")
# in 和 not in 和SQL中用法相同
list = [1,2,3,4,5,6,7,8,9,10]
a = 1
if a in list:
    print(True)
else:
    print(False)

print("====================")
# is 和 is not 象征的是判断两个地址引用是否相同
strIs = "123"
strIs2 = "123"
if strIs is strIs2:
    # 字符串是引用相同地址的，这点和Java相同
    print(True)
else:
    print(False)

numIs = 123
numIs2 = 123
if numIs is numIs2:
    # 数字是引用相同
    print(True)
else:
    print(False)

boolIs = True
boolIs2 = True
if boolIs is boolIs2:
    # 布尔值是引用相同的
    print(True)
else:
    print(False)

floatIs = 1.23
floatIs2 = 1.23
if floatIs is floatIs2:
    # 浮点数是引用相同的
    print(True)
else:
    print(False)

# 不难发现引用相同的都是基本类型数据
# is 类似于是否是同一个父类校验的功能
listIs = [1,2,3,4,5,6,7,8,9]
listIs2 = [1,2,3,4,5,6,7,8,9]
if listIs is listIs2:
    print(True)
else:
    # 列表是引用不相同的
    print(False)

# 结论：is 等同于 Java 的 == 判断 
#  == 等同于 Java 的 equals 判断

if listIs == listIs2:
    # 列表的值是相同的
    print(True)
else:
    print(False)
print("====================")

# 执行顺序是：
# 指数 - 位运算 - 乘除 - 加减 - 位移 - and 
# - 非 或 - 比较 - 判等 - 赋值 - 逻辑