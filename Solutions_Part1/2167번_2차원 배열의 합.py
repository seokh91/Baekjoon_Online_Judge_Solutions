import sys
n,m=map(int, sys.stdin.readline().split())
mat=[0]
for _ in range(n):
    mat.append([0]+list(map(int, sys.stdin.readline().split())))
points=[]
for _ in range(int(input())):
    points.append(tuple(map(int, sys.stdin.readline().split())))
for z in points:
    i,j,x,y=z[0],z[1],z[2],z[3]
    result=0
    for w in range(i, x+1):
        result+=sum(mat[w][j:y+1])
    print(result)
