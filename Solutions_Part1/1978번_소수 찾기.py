import sys

n=int(input())

def is_prime(num):
    judge=False; cnt=0
    for i in range(1,num+1):
        if num%i==0: cnt+=1
    if cnt==2:
        judge=True
        return judge
    else : return judge

l=list(map(int, sys.stdin.readline().split()))
cnt=0
for i in range(len(l)):
    if is_prime(l[i])==True : cnt+=1

print(cnt)
