import sys
n=int(input())
l=[sum(list(map(int, sys.stdin.readline().split(',')))) for _ in range(n)]
for i in l:
    print(i)
