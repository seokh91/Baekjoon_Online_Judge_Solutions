import sys
n=int(input())
l=list(map(int, sys.stdin.readline().split()))

max_num=max(l)
for i in range(n):
    l[i]=(l[i]/max_num)*100

result=sum(l)/n
print('%.2f'%result)
