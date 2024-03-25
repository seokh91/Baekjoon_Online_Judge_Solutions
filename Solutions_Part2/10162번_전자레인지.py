T=int(input())
result=[]

result.append(T//300)
T%=300
result.append(T//60)
T%=60
result.append(T//10)
T%=10

if T==0:
    for i in range(3): print(result[i],'',end='')

else: print(-1)

