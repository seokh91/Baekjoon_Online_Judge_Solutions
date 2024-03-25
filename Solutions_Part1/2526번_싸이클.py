n,p=map(int, input().split())
result=[(n*n)%p]; i=0 
while 1:
    if (result[i]*n)%p in result :
        start_index=result.index((result[i]*n)%p)
        end_index=i+1
        break
    result.append((result[i]*n)%p)
    i+=1
print(end_index-start_index)
