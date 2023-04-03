while True:
    s=input("请输入一段字符：")
    m=0
    for i in s:
        if i.isdigit():
            m+=1
    if m>0:
        print("输入字符中含有数字，请重新输入：")
    else:
        print(len(s))
        break
