s = eval(input("请输入一个数字："))
ls = []
for i in range(65, 91):
    ls.append(chr(i))
print("请输出字母：{}".format(ls[s-1]))
