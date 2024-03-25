import sys
n,k=map(int, sys.stdin.readline().rstrip('\n').split())

if k==0:
    print(1)
else :
    a,b=1,1
    for i in range(k):
        a=a*(n-i) ; b=b*(k-i)
    print(a//b)
