l=[]; length=0
n=int(input())
for i in range(n):
    l=l+list(input())
    if i==0 : length=len(l)
    
result=''; check=[]
for i in range(length):
    for j in range(1, n):
        if l[i]==l[i+length*j] : check.append(0)
        else : check.append(1)
    if check.count(1)==0 : result+=l[i]
    else : result+='?'
    check.clear()
print(result)
