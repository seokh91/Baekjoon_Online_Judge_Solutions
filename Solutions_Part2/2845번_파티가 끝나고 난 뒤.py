import sys
l,p=map(int, sys.stdin.readline().split())
peo=l*p
result=[int(v)-peo for v in sys.stdin.readline().split()]
for i in result:
    print(i, end=' ')
