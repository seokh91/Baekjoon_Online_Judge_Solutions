n,m=map(int, input().split())
temp=[]; result=[]; index=0
for i in range(1,n+1): temp.append(i)
while temp!=[]:
    index+=(m-1)
    index%=len(temp)
    result.append(temp.pop(index))
result=list(map(str, result))
print('<'+', '.join(result)+'>')
