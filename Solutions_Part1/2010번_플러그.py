import sys
n=int(input())
a=[sys.stdin.readline() for i in range(n)]
print(sum(list(map(int,a)))-n+1)
