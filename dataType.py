# 基础数据类型

num = 123
print(type(num))
str = 'hello'
print(type(str))
bool = True
print(type(bool))
list = [1, 2, 3]
print(type(list))
tuple = (1, 2, 3)
print(type(tuple))
setData = {1, 2, 3}
print(type(setData))
fractional = 1.2
print(type(fractional))
# dict = dictionary 作用与字典相同，key-value的形式
dict = {'a': 1, 'b': 2}
print(type(dict))
comp = 3+4J
print(type(comp))
print(isinstance(comp, complex))
# isinstance 和 type 的区别在于：
# type() 不会认为子类是一种父类类型。
# isinstance() 会认为子类是一种父类类型。

class Person:
    pass
class Student(Person):
    pass
print(isinstance(Student(), Person))
print(isinstance(Student(), object))
print(type(Person()) == Person)
print(type(Student()) == Person)

print("===========================================")
# 变量赋值
a = 123
print(a)
a = 'hello'
print(a)
a = True
print(a)

v = b = c = a
print(v, b, c)

v, b, c = 1, 2, 3
print(v, b, c)

v, b, c = 'test', 123, True
print(v, b, c)

# 删除值
var1 = 1
var2 = 2
del var1
print(var2)
# 此时打印var1会报错，询问你是否要找的是var2

# 字符串
str = 'Result'
print(str)
print(str.upper())
print(str.lower())
# 首字母大写
print(str.capitalize())
print(str.title())
print(str.strip())
print(str.rstrip())
print(str.lstrip())
print(str.find('u'))
# 找到最后一个出现的子字符串
print(str.rfind('u'))
print(str.count('u'))
print(str.index('u'))
print(str.replace('u', 'v'))

print("===========================================")
# list
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
# 不是强语言，所以集合兼容各种类型
print(list1 + list2)
print(list1[1:2])
print(list1[:2])
print(list1[-2:])
print(list1[-2:-1])
print(list1[:-2])
print(list1 * 2)
# list 可以更换index下对应的元素
# 且可以根据下标更换
print("===========================================")
# Tuple 和 List 相同的是都是集合
# 不同的是一个是不可变的(同字符串)，一个是可变的
tuple1 = ('a', 'b', 'c')
list1 = ['a', 'b', 'c']
tuple2 = (1, 2, 3)
list2 = [1, 2, 3]

# tuple允许拼接
print(tuple1 + tuple2)
print(tuple1[0])

# TypeError: 'tuple' object does not support item assignment
# tuple1[0] = 'd'
# print(tuple1)

print("===========================================")
# Set
# 注意：创建一个空集合必须用 set() 而不是 { }，
# 因为 { } 是用来创建一个空字典。
set1 = set()
set2 = {1, 2, 3}
set3 = {'a', 'b', 'c'}
# set 是无序但唯一的集合，元素不会出现重复值
set4 = {'a', 'b', 'c', 'a'}
print(set1)
print(set2)
print(set3)
print(set4)
print(set3 | set2)
if 'a' in set3:
    print('a' in set3)
else:
    print('a' not in set3)
# 差集
print(set2 - set3)
# 并集
print(set2 | set3)
# 交集
print(set2 & set3)
# 并集去重（重复数据干脆不存在）
print(set2 ^ set3)
print("===========================================")
# 字典 dict
dict1 = {}
dict1[0] = 'a'
print(dict1)
dict1['key'] = 'value'
print(dict1)

print(dict1.keys())
print(dict1.values())


print("===========================================")