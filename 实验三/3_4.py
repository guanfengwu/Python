import math

numB=input()

numBlength=len(numB)
a=numBlength-1
sum=0
  
while numB!=0:
    for x in range(a,4):      
        sum=sum+int(numB[x])*pow(2,a)
        a-=1
    numB=int(numB)%1000

print(sum)  
