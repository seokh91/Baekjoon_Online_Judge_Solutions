dic={1:[0,0,0,0,1], 2:[0,0,0,0,2], 3:[0,0,0,0,3]}
n=int(input())
for _ in range(n):
    a,b,c=map(int, input().split())
    dic[1][0]+=a; dic[2][0]+=b; dic[3][0]+=c
    dic[1][-a-1]+=1; dic[2][-b-1]+=1; dic[3][-c-1]+=1
temp=list(dic.values())
temp.sort(reverse=True)
if temp[0][0] != temp[1][0] : print(temp[0][4], temp[0][0])
elif temp[0][0] == temp[1][0] :
    if temp[0][1] != temp[1][1] : print(temp[0][4], temp[0][0])
    elif temp[0][1] == temp[1][1] :
        if temp[0][2] != temp[1][2] : print(temp[0][4], temp[0][0])
        elif temp[0][2] ==  temp[0][2] : print(0, temp[0][0])
