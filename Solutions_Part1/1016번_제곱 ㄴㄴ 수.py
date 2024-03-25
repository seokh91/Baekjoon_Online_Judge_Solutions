import math
import sys
mi,ma=map(int, sys.stdin.readline().split())
prime_pow=[]; result=list(range(mi,ma+1))

temp=int(math.sqrt(ma))
for i in range(1, temp+1):
    judge=True
    if i==1 : continue
    elif i==2 or i==3 :
        prime_pow+=[i*i]; continue
    elif i%2==0 : continue
    max_=math.sqrt(i)
    for j in range(3, int(max_)+1):
        if i%j==0 :
            judge=False; break
    if judge : prime_pow+=[i*i]

for i in prime_pow:
    if mi%i==0:
        portion=mi//i; temp=i*portion
    elif mi%i!=0:
        portion=(mi//i)+1; temp=i*portion
    while temp<=ma:
        result[temp-mi]=0
        temp+=i
cnt=0
for i in result:
    if i!=0:cnt+=1
print(cnt)
