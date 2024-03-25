import sys
n=int(input())
l=[]
for _ in range(n):
    n_1=int(input())
    l.append(list(map(int, sys.stdin.readline().split())))
for i in range(n):
    print(sum(l[i]))
