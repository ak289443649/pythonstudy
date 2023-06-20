# dict 独占空集合的命名方式
dictDemo = {}
print(type(dictDemo))
dictDemo2 = { 'name' : 'John', 'age' : 20 }
print(type(dictDemo2))

print(dictDemo2['name']) 
# dict 是不可以通过下标获取空值的，会报错 KeyError: 'test'
# print(dictDemo2['test'])

dictDemo2['test'] = 100
del dictDemo2['age']
print(dictDemo2)
dictDemo2.clear()
print(dictDemo2)
del dictDemo2

print("================================")
keyList = ['key1', 'key2', 'key3', 'key4']
noneDict = {}
copyDict = { 'key2' : 'value2' }
# fromKeys 方法会返回组装好的字典，这时需要我们进行赋值
noneDict = noneDict.fromkeys(keyList)
print(noneDict)
# 可以get方法获取没有的数据，但是不可以通过下标获取
key5Value = noneDict.get('key5')
print(key5Value)
# update 更新覆盖
noneDict.update(copyDict)
print(noneDict)

