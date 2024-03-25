import sys
n=int(input())
l=[]
for _ in range(n):
    a,b=sys.stdin.readline().split()
    l.append((int(a), int(b)))
for i in range(n):
    print('Case %d: %d'%(i+1,sum(l[i])))
