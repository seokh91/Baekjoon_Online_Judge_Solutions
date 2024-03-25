import sys
n=int(input())
a=list(map(int, sys.stdin.readline().split()))
cnt=0
for i in range(5):
    if a[i]==n : cnt+=1

print(cnt)
