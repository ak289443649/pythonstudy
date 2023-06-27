# path
import os
# 相对路径
print(os.getcwd())
# 根据相对路径打开文件 r可以让反斜杠保持不被转义
with open(r"demo-file\test.txt", "w") as f:
    f.write("Hello World")
# 实际路径
print(os.path.abspath("demo-file/test.txt"))
# join函数可以拼接路径
print(os.path.join("demo-file", "test.txt"))
# windows 下关于相对路径的调用也是同linux一样的
print(os.path.exists("demo-file/test.txt"))
# 文件详细信息
info = os.stat("demo-file/test.txt")
print(info.st_size)
print(info.st_mtime)
print("====")

walkTree = os.walk(r"demo-file")
print(type(walkTree))
iterator = iter(walkTree)
print(next(iterator))

tempPath = "temp-dir"
if not os.path.exists(tempPath):
    os.mkdir(tempPath)
    # os.chdir(tempPath)
os.rmdir(tempPath)

tempDirs = "temp/dir1/dir2/dir3"
os.makedirs(tempDirs)
# 1. os.rmdir(tempDirs)
import shutil
# 2. shutil.rmtree(tempDirs)
shutil.rmtree("temp")