a =input("请输入字符串：")
a=a.strip()
length=len(a)
for i in range(length-1 ,-1,-1):
    print(a[i],end="")
