
var=eval(input("请输入一个整数："))


def countsum(var):
    sum=0
    while(True):
        sum=sum+var%10
        var=int(var/10)
        if(var==0):
            return sum

print(countsum(var))

