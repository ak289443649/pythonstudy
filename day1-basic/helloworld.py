print('helloworld1')
# 注释的几种使用形式
'''
 description
'''

"""
description
"""

print('helloworld2')

# 缩进即为代码块，缩进格数不同会报错
if True:
    print   ("True")
else:
    print   ("False")

# 多行字符串换行需要使用反斜杠
str = "test" + \
    "_test_" + \
    "test"
print(str)

# 数组集合类型无需换行
arr = [1, 2, 3]
print   (arr)

obj = {
    "name": "zhangsan",
    "age": 18
}
print(obj)