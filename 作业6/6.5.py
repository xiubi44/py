from random import *
yes, no, p, asd,option = 0, 0, 0, 0, 1
n = input("请输入题目数量：")
while option == 1:
    v,a = randint(0, 1),randint(0, 20)
    b = randint(0, 20 - a)
    p += 1
    while 1:
        try:
            if v == 0:
                c = a + b
                d = input("请输入{}+{}=".format(a, b))
            else:
                if a < b:
                    a, b = b, a
                c = a - b
                d = input("请输入{}-{}=".format(a, b))
            if int (d) != c:
                asd = 1
                print("错误，重新计算！")
            else:
                if asd != 1:
                    yes += 1
                    print("正确!")
                else:
                    asd = 0
                break
        except:
            print("输入非法字符，请输入数字!")
    option = eval(input("是否继续？（输入,1继续，0退出系统。）"))
k = int(n) - p
if k >= 0:
    print("计算结束,正确率为{:.2%},未完成的题目数量还有{}道".format(yes / p, k))
else:
    print("计算结束,正确率为{:.2%},多完成的题目数量有{}道".format(yes / p, -k))
