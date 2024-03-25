l=[0]; n=int(input())
for i in range(1,3164):
    temp=(i*(i+1))//2
    if temp >= n :
        l.append(temp)
        break
    l.append(temp)
result=[]
for i in range(1, len(l)):
    result.append((i, len(l)-i))
if (len(l)-1)%2==0: ans=str(result[n-(l[len(l)-2]+1)][0])+'/'+str(result[n-(l[len(l)-2]+1)][1])
else : ans=str(result[l[len(l)-1]-n][0])+'/'+str(result[l[len(l)-1]-n][1])
print(ans)
