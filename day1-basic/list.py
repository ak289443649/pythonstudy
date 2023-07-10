# Lists all
from collections import deque


arr = [1,2,3,4,5,6]
for i in arr:
    print(i)
    if i == 3:
        break

print("next")

arr[2] = 1
del arr[3]
print(arr) # [1, 2, 1, 5, 6]

length = len(arr)
print(length)

arr = arr + [9,99]
print(arr)

newArr = [1,2] * 2
print(newArr)

if 99 in arr:
    print("yes")
else:
    print("no")

print("length : {}".format(arr.count(1)))

print("max : {}".format(max(arr)))
# reverse 只负责将集合进行倒置，并不负责排序，也没有返回值
arr.reverse()
print("reversed : {}".format(arr))

copyArr = arr.copy()
print(copyArr)

print("==========================")
tupleArr = 1,2,3
print(type(tupleArr))

tup1 = ()
print(type(tup1))

# tuple 起始如果仅有一个元素，那么就是那个元素的类型，而集合恒为集合
intTup = (1)
strTup = "hello"
intList = [1]
print(type(intTup))
print(type(strTup))
print(type(intList))
intTup = (1,2,3)
intList = [1,2,3]
print(type(intTup))
print(type(intList))
# 以下表达式会报错，因为元组不可变
# intTup[0] = 10

list = [1,2,3]
list.append(4)
print(list)

list.extend([5,6])
print(list)

list.insert(0, 0)
print(list)

# 将list作为stack使用
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)

stack.pop()
print(stack)

# 将list作为queue使用
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)

queue.popleft()
print(queue)

print("==========================")
# list other methods
list = [1,2,3]
list1 = [4,5,6]
# 1. zip()
for i in zip(list, list1):
    print(i)
    print(i[0])
    print(i[1])

# 2. reverse()
for i in reversed(list):
    print(i)
list = [3,2,1]
# 3. sort() 默认 ASC
for i in sorted(list):
    print(i)


list = [1,2,3,4,5,6]
list.append(7)
list.remove(6)
print(list)

print("==========================")

def add_end(L=[]):
    L.append('END')
    return L

for i in range(2):
    print(add_end())