import sys
n=int(input())
l=[list(map(int, sys.stdin.readline().split())) for _ in range(2)]
result=0
for _ in range(n):
    a,b=min(l[0]), max(l[1])
    result+=(a*b)
    l[0].remove(a); l[1].remove(b)
print(result)
