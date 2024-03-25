import sys
import math
n=int(input())
l=[tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

def distance(points):
    result=math.sqrt((points[0]-points[3])**2 +(points[1]-points[4])**2)
    return result

for t in l :
    dis=distance(t)
    if t[0]==t[3] and t[1]==t[4] and t[2]==t[5] : print(-1)
    elif dis > (t[2]+t[5]) or dis < abs(t[2]-t[5]): print(0)
    elif dis == (t[2]+t[5]) or dis == abs(t[2]-t[5]): print(1)
    elif abs(t[2]-t[5]) < dis and dis < (t[2]+t[5]): print(2)
