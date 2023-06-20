# if else
str = "hello"
if str == "hello":
    print("hello")
elif str == "test":
    print("test")
else:
    print("world")

a = 10
while a < 100:
    print(a)
    a += 1
else:
    print("done")

# break and continue 和Java相同
list = [1, 2, 3, 4, 5]
for i in list:
    if i == 3:
        print("done")
        continue
    elif i == 5:
        print("exit")
        break
    else:
        print(i)