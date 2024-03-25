n=int(input()); l=[]; result=[]
for i in range(n):l.append(int(input()))
for i in range(len(l)-1):
    for j in range(i+1, len(l)):
        result.append(l[i]^l[j])
print(sum(result))
