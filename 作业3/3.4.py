for i in range(1000, 10000):
    a = str(i)
    if a[0] == a[-1] and a[1] == a[-2]:
        print(i)