import sys
n=int(input())
l=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in l :
    i.sort(reverse=True)
    print(i[2])
