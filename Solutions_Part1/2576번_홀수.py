import sys
a=[int(sys.stdin.readline()) for _ in range(7)]
b=[i for i in a if i%2!=0]

if len(b)==0 : print(-1)
else :
    print(sum(b))
    print(min(b))
