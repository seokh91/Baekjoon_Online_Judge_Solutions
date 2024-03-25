import math
m=int(input()); n=int(input())
l=[]

for i in range(m,n+1):
    if int(math.sqrt(i))**2==i:
        l.append(i)

if len(l)==0:
    print(-1)
else:
    print(sum(l))
    print(l[0])
