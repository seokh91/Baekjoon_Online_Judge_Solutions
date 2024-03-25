import sys
l=[]
for _ in range(int(input())):
    x,y=map(int, sys.stdin.readline().split())
    l.append((y,x))
l.sort()
for i in l: print(i[1],i[0])
