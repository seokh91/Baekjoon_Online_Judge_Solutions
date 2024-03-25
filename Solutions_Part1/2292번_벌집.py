n=int(input())
l=[1]
if n==1:print(1)
else :
    term=6
    while l[-1]+term <= n :
        l.append(l[-1]+term)
        term+=6
    if l[-1] == n : print(len(l))
    else : print(len(l)+1)
