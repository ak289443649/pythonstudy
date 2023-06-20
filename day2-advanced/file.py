# file

# open
# file mode hava 5 r w x a b + 代表拥有了写的权限
# 没有指定具体路径，生成的文件默认放在项目最外层
file = open('test.txt', 'w')
# open方式打开文件必须使用close进行关闭
file.close()

# with open
with open('test.txt', 'w') as file:
    file.write('hello world')

# 读取文件
with open('test.txt', 'r') as file:
    file.seek(1)
    content = file.read(4) # ello
    print(content)

# readline
# readlines

with open('test.txt', 'r') as file:
    for line in file.readlines():
        print(line)
