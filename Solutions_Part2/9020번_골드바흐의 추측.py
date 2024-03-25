from math import *
def is_prime(num):
    if num==1 : return False
    elif num==2 or num==3: return True
    elif num%2==0 : return False
    for i in range(3, int(sqrt(num))+1):
        if num%i==0 : return False
    return True

n=int(input())
l=[]; max_prime=[]
for _ in range(n):
    l.append(int(input()))
    
max_num=max(l)
for i in range(2, max_num):
    if is_prime(i) : max_prime.append(i)

for i in l:
    temp=[]
    for j in max_prime :
        if j+j>i : break
        if is_prime(abs(i-j)) :
            temp.append((j, i-j))
    k=min(temp, key=lambda item: abs(item[1]-item[0]))
    print(k[0],k[1])
