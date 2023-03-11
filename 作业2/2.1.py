ls = ["鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡", "狗", "猪"]
# print(len(ls))
n = eval(input("n="))
print("{}".format(ls[(n - 4) % 12]))
