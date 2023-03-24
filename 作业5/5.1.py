x = input("请输入2个正整数(空格分隔):")
ls = x.split()
a = eval(ls[0])
b = eval(ls[1])
def c(a: int, b: int):
    if b == 0:
        return a
    else:
        return c(b, a % b)
print("最小公倍数为:{}".format(c(a,b)))
print("最大公约数为:{}".format(a*b/c(a,b)))