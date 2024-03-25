l=[]; cnt=0
n=int(input())
for _ in range(n):
    a=input()
    l.append(list(a))

def sumation(cnt):
    result=0
    for i in range(cnt+1):
        result+=i
    return result

for i in range(n):
    result=0
    for j in range(len(l[i])):
        if l[i][j]=='O':
            cnt+=1
        if l[i][j]=='X' or j==len(l[i])-1:
            result+=sumation(cnt)
            cnt=0
    print(result)
