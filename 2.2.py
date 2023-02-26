print('请输入需要反向输出的字符串', end="：")
b = input()
d = "反向输出的字符串为："
length = len(b)
# print(length)
for i in range(length + 1):
    d = d + b[length - i: length - i + 1]
print(d)
