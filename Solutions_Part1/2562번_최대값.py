import sys
l=[int(sys.stdin.readline()) for _ in range(9)]
print(max(l))
print(l.index(max(l))+1)
