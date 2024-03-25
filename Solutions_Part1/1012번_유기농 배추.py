import sys
from sys import setrecursionlimit
sys.setrecursionlimit(1000000)

def search(x,y):

    ground[x][y]=0
        
    if x+1<=size[1]-1 and ground[x+1][y]==1:
        search(x+1, y)
    if x-1>=0 and ground[x-1][y]==1:
        search(x-1, y)
    if y+1<=size[0]-1 and ground[x][y+1]==1:
        search(x, y+1)
    if y-1>=0 and ground[x][y-1]==1:
        search(x, y-1)

for _ in range(int(input())):
    size=tuple(map(int, sys.stdin.readline().rstrip('\n').split()))
    ground=[]
    for _ in range(size[1]):
        ground.append([0]*size[0])
    for _ in range(size[2]):
        place=tuple(map(int, sys.stdin.readline().rstrip('\n').split()))
        ground[place[1]][place[0]]=1

    cnt=0
    for i in range(size[1]):
        for j in range(size[0]):
            if ground[i][j]==1:
                search(i,j)
                cnt+=1

    print(cnt)
    ground.clear()
