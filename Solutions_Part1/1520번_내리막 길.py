import sys
m,n=list(map(int, sys.stdin.readline().rstrip('\n').split()))
mat=[] ; dp=[] ; stack=[]
for _ in range(m):
    mat.append(list(map(int, sys.stdin.readline().rstrip('\n').split())))
    dp.append([-1 for _ in range(n)])

