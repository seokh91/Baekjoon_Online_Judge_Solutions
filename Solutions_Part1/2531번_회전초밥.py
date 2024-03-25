n,d,k,c=map(int, input().split())
l=[]; result=[]
for _ in range(n):
    l.append(int(input()))
l+=l[0:k-1]
for i in range(len(l)-k+1):
    temp=set(l[i:i+k])
    if c in temp : result.append(len(temp))        
    elif c not in temp :
        result.append(len(temp)+1)
        if len(temp)+1 == k+1 : break
print(max(result))
