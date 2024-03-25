import sys
a,b=sys.stdin.readline().split()
a=int(a); b=int(b)

l=[]; cnt=0; i=1; z=1; judge=True
while judge:
    for j in range(1, i+1):
        l.append(z)
        cnt+=1
        if cnt == b :
            judge=False
            break
    i+=1
    z+=1
    
result=0
for i in range(a,b+1):
    result+=l[i-1]

print(result)
