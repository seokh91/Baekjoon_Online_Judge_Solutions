import sys

n,a,b=list(map(int, sys.stdin.readline().rstrip().split()))
cnt_a=0 ; cnt_b=0

while abs(a-b)!=1 or max(a,b)%2!=0 :
    if a%2!=0 : a+=1
    if b%2!=0 : b+=1
    a//=2 ; cnt_a+=1
    b//=2 ; cnt_b+=1

print(max(cnt_a, cnt_b)+1)
