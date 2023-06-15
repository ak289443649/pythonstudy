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

# 按下回车后会返回
input("\n\n check enter exit...")