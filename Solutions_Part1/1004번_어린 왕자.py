import sys
from math import*

def check(a,b,r,x,y):
    if pow((x-a),2) + pow((y-b),2) < pow(r,2) : return True
    else : False

result=[]
for _ in range(int(input())):
    x1,y1,x2,y2=map(int, sys.stdin.readline().split())
    cnt=0
    for _ in range(int(input())):
        a,b,r=map(int, sys.stdin.readline().split())
        if check(a,b,r,x1,y1) : cnt+=1
        if check(a,b,r,x2,y2) : cnt+=1
        if check(a,b,r,x1,y1) and check(a,b,r,x2,y2) : cnt-=2
    result.append(cnt)
for i in result:
    print(i)
