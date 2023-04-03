from random import *
a=randint(0,10)
print("请输入你猜测的数字：")
b=eval(input())
count=1
while True:
    if a==b:
        print("猜测次数为{}".format(count))
        break
    else:
        count+=1
        b=eval(input("请再次猜测："))



