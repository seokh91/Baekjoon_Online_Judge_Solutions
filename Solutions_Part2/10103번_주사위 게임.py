n=int(input())
l=[]
for _ in range(n):
    a,b=input().split()
    a=int(a); b=int(b)
    l.append((a,b))

cp=100; sp=100

for i in range(len(l)):
    if l[i][0] > l[i][1]: sp-=l[i][0]
    elif l[i][0] < l[i][1]: cp-=l[i][1]

print(cp)
print(sp)
