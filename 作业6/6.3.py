from random import *
while True:
    a = randint(0, 20)
    b = randint(0, 20 - a)
    print("{}+{}=".format(a, b))
    c = eval(input())
    if c==a+b:
        print("回答正确，是否继续计算？（1为是，0为否）")
        d=eval(input())
        while True:
            if d==1:
                break
            if d==0:
                break
        if d == 0:
            break
    else:
        c=eval(input("回答错误，请再次输入："))