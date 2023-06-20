# Set 集合 无序 不重复
set1 = {1, 2, 3, 4, 5, 6}
# Set 无法进行空花括号的声明，因为那是属于Dict的

set1.add(7)
print(set1)
set1.remove(7)
print(set1)

set2 = set(('a', 'b', 'c', 'd', 'e'))
print(set2)

# 减号就是差集
set1 = set1 - set2
# remove同样不可对不存在的key进行remove，会报错
# 可以使用替换函数 discard
# set1 = set1.remove(7)
# set remove 无需进行赋值
set2.remove('b')
print(set2)
set1.discard(3)
print(set1)
# difference_update() 方法称为“就地差集” 
# 可以更新set1为去掉差集结果的集合
set1.difference_update(set2)

