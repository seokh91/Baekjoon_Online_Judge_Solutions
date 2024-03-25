import sys
T=int(input())
s=[]; pig=[]
for _ in range(T):
    s.append(int(input()))
    pig.append(list(map(int, sys.stdin.readline().split())))

for i in range(T):
    days=1; temp=pig[i].copy()
    while s[i] >= sum(pig[i]):
        days+=1
        for j in range(6):
            if j % 2 == 0: pig[i][j] = (temp[j]+temp[1]+temp[3]+temp[5])
            else : pig[i][j] = (temp[j]+temp[0]+temp[2]+temp[4])
        temp=pig[i].copy()
    print(days)
