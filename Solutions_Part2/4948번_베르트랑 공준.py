from math import *
def is_prime(num):
    if num==1 : return False
    elif num==2 or num==3 : return True
    elif num%2==0 : return False
    else :
        for i in range(3, int(sqrt(num))+1):
            if num%i==0: return False
    return True

l=[]; prime=[]; max_num=0
while 1:
    a=int(input())
    if a==0: break
    l.append(a)
max_num=max(l)
for i in range(1, 2*max_num+1):
    if is_prime(i) : prime.append(i)
for i in l :
    cnt=0
    for j in prime:
        if i<j and j<=2*i : cnt+=1
    print(cnt)
