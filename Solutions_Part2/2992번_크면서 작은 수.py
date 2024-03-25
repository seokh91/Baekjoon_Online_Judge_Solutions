n=list(input()) ; left=len(n)-1 ; flag=False

for i in range(left, 0, -1):
    if n[i-1]<n[i]:
        a=sorted(n[i:])
        for j in a :
            if j > n[i-1] :
                flag=True ; idx=n[i:].index(j)+(len(n)-len(n[i:]))
                temp=n[i-1]
                n[i-1]=n[idx]
                n[idx]=temp
                n[i:]=sorted(n[i:])
                break
        if flag : break

if not flag : print(0)
else : print(''.join(n))
