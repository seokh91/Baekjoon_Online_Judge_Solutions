import sys
n=int(input())
a=list(map(int, sys.stdin.readline().split()))
result=0; cnt=0

def sumation (num):
    result=0
    for i in range(1,num+1):
        result+=i
    return result

for i in range(len(a)):
    if a[i]==1 : cnt+=1
    elif a[i]==0 :
        result+=sumation(cnt)
        cnt=0
    if i==len(a)-1:
        result+=sumation(cnt)
    
print(result)
