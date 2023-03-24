from random import*
a=b=0
c=eval(input("请输入样本次数:"))
for i in range(c):
    m=randint(0,2)
    n=randint(0,2)
    if m!=n:
        a+=1
    else:
        b+=1
print("改变选择获胜的概率为：{}，不改变选择获胜的概率为{}".format(a/c,b/c))

