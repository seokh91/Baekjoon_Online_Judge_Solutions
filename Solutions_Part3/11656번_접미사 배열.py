s=input(); length=len(s); result=[]
for i in range(length):
    result.append(s[i:])
for i in sorted(result): print(i)
