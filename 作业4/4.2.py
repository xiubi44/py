s=input("请输入一段字符(空格分隔)：")
s=s.replace(" ", "")
m=len(s)
for i in range(m):
    print("{}".format(chr(ord("a")+(ord(s[i])-ord("a")+5)%26)),end=" ")