import sys
a=list(map(int, sys.stdin.readline().split()))
result=0
for i in range(len(a)):
    result+=(a[i])**2
print(result%10)
