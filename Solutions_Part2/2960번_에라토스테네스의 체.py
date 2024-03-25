import math
n,k=map(int, input().split())
temp=[0]*(n+1)

def is_prime(num):
    if num==1:return False
    if num==2 or num==3:return True
    elif num%2==0:return False
    max_=math.sqrt(num)
    for i in range(3, int(max_)+1):
        if num%i==0:return False
    return True

cnt=0; judge=False
for i in range(2,n+1):
    if is_prime(i):
        term=i
        while term<=n :
            if temp[term]==0 :
                cnt+=1; temp[term]=cnt
            term+=i
            if cnt==k :
                judge=True; break
    if judge : break

print(temp.index(cnt))
