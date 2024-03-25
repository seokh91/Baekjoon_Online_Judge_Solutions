import sys
n=int(input())
l=list(map(int, sys.stdin.readline().split()))
if len(l)==1:
    print(l[0]*l[0])
else :
    l.sort()
    print(l[0]*l[len(l)-1])
