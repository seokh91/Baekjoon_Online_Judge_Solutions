l=[]
n=int(input())
for _ in range(n):
    a,b=input().split()
    a=int(a); b=int(b)
    l.append((a,b))

result=0
for i in range(n):
    if l[i][0] > l[i][1] : result+=l[i][1]
    else : result+= l[i][1]%l[i][0]

print(result)
