import sys
n=int(input())
l=list(map(int, sys.stdin.readline().split()))
find=int(input())

print(l.count(find))
