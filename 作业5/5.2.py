s = input("请输入一个字符串:")
a = 0
b = 0
c = 0
d = 0

for i in s:
    if i.isalpha():
        a += 1
    elif i.isdigit():
        b += 1
    elif i.isspace():
        c += 1
    else:
        d += 1
print("字母有{}个，数字有{}个，空格有{}个，其他字符有{}个。" .format(a, b, c, d))
