import sys
line=list(map(int, sys.stdin.readline().split()))
check=[0]*33554432; result=[]
for i in line:
    if check[i]==0:
        check[i]+=1
        result.append(i)
    else : continue
for i in result:
    print(i, end=' ')
