# Lists all
arr = [1,2,3,4,5,6]
for i in arr:
    print(i)
    if i == 3:
        break

print("next")

# python data types : int, float, bool, complex复数
num = 0
print("number", num)

flag = False
print("flag", flag)

flo = 1.2
print("flo", flo)

# python 单引号和双引号使用相同

# r可以让转义符失效
print("r", r"\n")
print("r", r"\t")
print("r", r"\'")
print("n r", "\"")
print("n r", "\n")
print("n r", "\t")

print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义