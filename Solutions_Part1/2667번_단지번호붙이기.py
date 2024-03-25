import sys
n=int(input()) ; map_home=[] ; res=[]
for _ in range(n):
    map_home.append(list(map(int, list(sys.stdin.readline().rstrip('\n')))))

def search(x, y):
    global cnt
    cnt+=1 ; map_home[x][y]=2
    
    if x+1 < n and map_home[x+1][y]==1 :
        search(x+1, y)
    if x-1 >= 0 and map_home[x-1][y]==1 :
        search(x-1, y)
    if y+1 < n and map_home[x][y+1]==1 :
        search(x, y+1)
    if y-1 >= 0 and map_home[x][y-1]==1 :
        search(x, y-1)

for i in range(n):
    for j in range(n):
        if map_home[i][j]==1 :
            cnt=0
            search(i,j)
            res.append(cnt)

print(len(res))
for i in sorted(res) :
    print(i)
