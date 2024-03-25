lower='abcdefghijklmnopqrstuvwxyz'
upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s=list(input())
for i in range(len(s)):
    if s[i] in upper:
        if upper.index(s[i])+13 > 25:
            s[i]=upper[(upper.index(s[i])+13)%26]
        else:
            s[i]=upper[upper.index(s[i])+13]
    elif s[i] in lower:
        if lower.index(s[i])+13 > 25:
            s[i]=lower[(lower.index(s[i])+13)%26]
        else:
            s[i]=lower[lower.index(s[i])+13]
result=''
for i in s:
    result+=i
print(result)
