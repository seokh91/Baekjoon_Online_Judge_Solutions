import sys
n=int(input())
l=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in l:
    even=[]
    for j in i:
        if j%2==0: even.append(j)
    print(sum(even), min(even))
