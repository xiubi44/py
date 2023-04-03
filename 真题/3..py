s=input("请输入：")
count=0
for i in s:
    if (0x4e00 <= ord(i) <= 0x9fa5):
        count+=1
print(count)