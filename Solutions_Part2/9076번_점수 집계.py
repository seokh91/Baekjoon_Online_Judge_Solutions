import sys
n=int(input())
l=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in l:
    i.sort()
    if i[3]-i[1] >= 4 : print('KIN')
    else : print(i[1]+i[2]+i[3])
