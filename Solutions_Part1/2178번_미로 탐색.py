import sys
n,m=list(map(int, input().split()))
miro=[] ; res=[] ; trace=[] ; stack=[(0,0,1)]
for _ in range(n):
    miro.append(list(map(int, list(sys.stdin.readline().rstrip('\n')))))

while stack != [] :
    loc=stack.pop() ; miro[loc[0]][loc[1]]=2 ; trace.append((loc[0], loc[1]))

    if loc[0]==n-1 and loc[1]==m-1 :
        res.append(loc[2])
        for i in trace : miro[i[0]][i[1]]=1
        trace=[] ; stack=[] ;

    else :
        if loc[0]+1 < n and miro[loc[0]+1][loc[1]]==1 :
            stack.append((loc[0]+1, loc[1], loc[2]+1))
        if loc[0]-1 >= 0 and miro[loc[0]-1][loc[1]]==1 :
            stack.append((loc[0]-1, loc[1], loc[2]+1))
        if loc[1]+1 < m and miro[loc[0]][loc[1]+1]==1 :
            stack.append((loc[0], loc[1]+1, loc[2]+1))
        if loc[1]-1 >= 0 and miro[loc[0]][loc[1]-1]==1 :
            stack.append((loc[0], loc[1]-1, loc[2]+1))
        
