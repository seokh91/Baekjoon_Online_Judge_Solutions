import sys
input() ; r1=0 ; r2=0
a=[abs(i) for i in map(int, sys.stdin.readline().rstrip('\n').split())]
b=[-abs(i) for i in map(int, sys.stdin.readline().rstrip('\n').split())]
print(sum(a)-sum(b))
