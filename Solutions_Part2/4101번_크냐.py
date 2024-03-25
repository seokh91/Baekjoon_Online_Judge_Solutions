import sys
l=[]
while True:
    r=lambda :sys.stdin.readline()
    a,b=map(int, r().split())
    if a==0 and b==0: break
    l.append((a,b))

for i in range(len(l)):
    if l[i][0]>l[i][1]: print('Yes')
    else: print('No')

