n,k=input().split()
n=int(n); k=int(k)

l=[]
for i in range(1,n+1):
    if n%i==0: l.append(i)

if len(l) < k : print(0)
else : print(l[k-1])
