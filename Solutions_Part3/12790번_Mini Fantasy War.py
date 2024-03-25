import sys
n=int(input())
l=[tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in l :
    result=0
    hp=i[0]+i[4]; mp=i[1]+i[5]
    attack=i[2]+i[6]; defen=i[3]+i[7]
    if hp<1 : hp=1
    if mp<1 : mp=1
    if attack<0 : attack=0
    result+=(hp+5*mp+2*attack+2*defen)
    print(result)
