import sys
import math as m

n=int(sys.stdin.readline().rstrip()) ; temp=n

res=1
for i in range(2, int(m.sqrt(temp))+1):
    if n%i!=0 : continue
    else :
        cnt=0
        while n%i==0 :
            cnt+=1 ; n//=i
        res*=(i**cnt-i**(cnt-1))

if n!=1 : res*=(n-1)
print(res)
