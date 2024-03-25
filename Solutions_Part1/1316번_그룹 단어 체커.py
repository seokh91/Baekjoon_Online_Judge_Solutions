import sys
n=int(input())
l=[list(sys.stdin.readline().rstrip('\n')) for _ in range(n)]
cnt=len(l)

for i in l :
    temp=''
    for j in i :
        if j not in temp or temp[len(temp)-1]==j :
            temp+=j
        else :
            cnt-=1
            break
print(cnt)
