n=int(input())
l=[]
for a in range(n//5+1):
    for b in range(n//3+1):
        if (5*a+3*b)==n:
            l.append(a+b)

if len(l)==0: print(-1)
else : print(min(l))
