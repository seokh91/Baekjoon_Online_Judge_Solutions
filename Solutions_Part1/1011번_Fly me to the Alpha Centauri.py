import sys
import math as m

l=[]
for _ in range(int(input())):
    l.append(tuple(map(int, sys.stdin.readline().rstrip('\n').split())))

for i in l:
    dist=i[1]-i[0] ; th=int(m.sqrt(dist))
    left=th**2 ; right=(th+1)**2

    if dist >= left + (right-left+1)//2 : print(2*th+1)
    elif left+1 <= dist and dist < left + (right-left+1)//2 : print(2*th)
    elif dist == left : print(2*th-1)
