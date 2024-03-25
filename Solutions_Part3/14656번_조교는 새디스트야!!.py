import sys
input()
a=list(map(int, sys.stdin.readline().rstrip('\n').split()))
cnt=0
for i in a :
    if a.index(i)+1 != i : cnt+=1
print(cnt)
