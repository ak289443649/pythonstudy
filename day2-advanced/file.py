# file 
# with 被称之为上下文处理器，可以在文件中进行读写操作。
# with 还可以被用于数据库的连接处理

# open
# file mode 有五种 r w x a b 后面附加加号“+” 代表赋予了写的权限
# r read 读取 、 w write 写入 、 a append 追加 、 b binary 二进制 
# x 模式比较特殊，是一种”独占“模式，当且仅当该文件不存在时可以使用，否则会出现文件存在异常
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
