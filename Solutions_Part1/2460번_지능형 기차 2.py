import sys
l=[tuple(map(int, sys.stdin.readline().split())) for _ in range(10)]
l_1=[i[1]-i[0] for i in l]

for i in range(1,10):
    l_1[i]+=l_1[i-1]

print(max(l_1))
