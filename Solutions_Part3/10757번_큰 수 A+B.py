a,b=input().split()
a=list(a); b=list(b)

for i in range(len(a)):
    a[i]=int(a[i])
for i in range(len(b)):
    b[i]=int(b[i])
    
result=[]

if len(a) > len(b) :
    length=len(a)
    for i in range(1, length):
        if i <= len(b):
            result.append((a[-i]+b[-i])%10)
            if a[-i]+b[-i]>=10 : a[-(i+1)]+=1
        elif i > len(b) and i < len(a):
            result.append(a[-i]%10)
            a[-(i+1)]+=a[-i]//10
    result.append(a[-length])

elif len(a) == len(b) :
    for i in range(1, len(a)):
        result.append((a[-i]+b[-i])%10)
        if a[-i]+b[-i]>=10 : a[-(i+1)]+=1
    result.append(a[-len(a)]+b[-len(b)])
    
elif len(a) < len(b) :
    length=len(b)
    for i in range(1, length):
        if i <= len(a):
            result.append((a[-i]+b[-i])%10)
            if a[-i]+b[-i]>=10 : b[-(i+1)]+=1
        elif i > len(a) and i < len(b):
            result.append(b[-i]%10)
            b[-(i+1)]+=b[-i]//10
    result.append(b[-length])        

sol=''
for i in range(1,len(result)+1):
    sol+=str(result[-i])

print(sol)
