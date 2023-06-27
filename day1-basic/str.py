str = 'test string'

print(str * 2)
print(str[0])
print(str.upper())
str = str.upper()
print(str.lower())
str = str.lower()
str = str.replace('s','x')
print(str)
# [param1,param2,param3] param1 is start, param2 is end
# param3 is step size
# index start at 0
print(str[1::2])
# step == -1 反向遍历字符串
print(str[::-1])
# r 会使转义符失效
print('hello\n world')
print(r'hello\n world')

# 关于字符串函数 
# - 字符串替换
print("================================")
print("str0 : %d" % len(str))

print("str1 : {}".format("test string"))

print("str2 : {name}".format(name = str))

# - 其他函数
print("================================")
str = "test string"
findFlag = str.find('test')
if findFlag!= -1:
    print("findFlag : %d" % findFlag)
else:
    print("not find")

fileName = "python.txt"
endWithFlag = fileName.endswith('.txt')
print(endWithFlag)
# find 和 index作用相同，但是index不允许空值的出现
indexFlag =str.index('test')
print(indexFlag)

# istitle() 方法作用是判断该字符串的格式类型是否等同于英文标题
str1 = "The Quick Brown Fox Jumps Over The Lazy Dog"
print(str1.istitle())  # True

str2 = "The quick Brown Fox Jumps Over The Lazy Dog"
print(str2.istitle())  # False

str3 = "This Is A Single-Word Title"
print(str3.istitle())  # True

lowerStr = 'abc'
upperStr = 'ABC'
print(lowerStr.islower())  # True
print(upperStr.islower())  # False

print(lowerStr.isupper())  # False
print(upperStr.isupper())  # True

list = ['a', 'b', 'c']
joinStr = ','.join(list)
print(joinStr)

print("================================")
str = " test "
print(str.strip())
print(str.lstrip())
print(str.rstrip())
# strip() 移除字符串头尾空格 也不会自动赋值 需要手动赋值
str = str.strip()
print(len(str))

print("================================")
str = max(upperStr)
print(str)

str = min(upperStr)
print(str)

print("================================")
# 截取
# 1.功能三个参数分别是：start, end, step
# 2.且同Java中的截取相同，均为左闭右开区间
subStr = "test demo python"
print(subStr[0:3])
print(subStr[0:5:1])
print(subStr[0:6:1])
print(subStr[-1:-7:-1])
print(subStr[-6::1])