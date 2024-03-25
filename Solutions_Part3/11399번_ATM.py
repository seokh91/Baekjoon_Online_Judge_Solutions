import sys
n=int(input())
l=sorted(list(map(int, sys.stdin.readline().rstrip('\n').split())))
cost=0
for i in range(n):
    for j in range(i+1):
        cost+=l[j]

print(cost)
