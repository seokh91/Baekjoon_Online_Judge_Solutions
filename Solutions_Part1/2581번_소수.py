a=int(input())
b=int(input())

def is_prime(num):
    cnt=0; judge=False
    for i in range(1,num+1):
        if num%i==0: cnt+=1
    if cnt==2:
        judge=True
        return judge
    else :
        return judge

l=[]
for i in range(a,b+1):
    if is_prime(i)==True : l.append(i)

if len(l)==0 : print(-1)
else:
    print(sum(l))
    print(min(l))
