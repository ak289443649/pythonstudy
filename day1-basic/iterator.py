import sys


list = [1, 2, 3, 4, 5, 6, 7]
it = iter(list)

# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         # StopIteration 会标识该迭代器迭代完成
#         sys.exit()

class MyIterator(object):
    # def __init__(self, iterable):
    #     self.iterable = iterable
    #     self.index = 0
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a < 10:
            num = self.a
            self.a += 1
            return num
        else:
            # raise thrown exception
            raise StopIteration
    
iterator = MyIterator()
it = iter(iterator)

for i in it:
    print(i)

def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成
 
while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()