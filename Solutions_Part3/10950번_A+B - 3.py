n=int(input())
l=[]
for _ in range(n):
    a,b=input().split()
    a=int(a); b=int(b)
    l.append(a+b)

for i in range(n):
    print(l[i])
