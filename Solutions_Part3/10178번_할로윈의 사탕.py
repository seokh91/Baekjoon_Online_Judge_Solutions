import sys
n=int(input())
l=[]
for _ in range(n):
    a,b=sys.stdin.readline().split()
    l.append((int(a), int(b)))
for i in range(n):
    print('You get %d piece(s) and your dad gets %d piece(s).'%(l[i][0]//l[i][1], l[i][0]%l[i][1]))
