import sys

n,_=list(map(int, sys.stdin.readline().rstrip().split()))
loca=list(map(int, sys.stdin.readline().rstrip().split()))
res=0

while loca!=[]:
    tmp=loca.pop(0)
    if tmp-1 <= n-tmp:
        res+=(tmp-1)
        for i in range(len(loca)):
            loca[i]-=tmp
            loca[i]=loca[i]%n
    else :
        res+=(n-tmp+1)
        for i in range(len(loca)):
            loca[i]+=(n-tmp)
            loca[i]=loca[i]%n
    n-=1
print(res)
