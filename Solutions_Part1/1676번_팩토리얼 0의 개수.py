import sys

def factorial(n):
    res=1
    for i in range(n, 0, -1):
        res*=i
    return res

n=str(factorial(int(sys.stdin.readline().rstrip()))) ; cnt=0

for i in range(1, len(n)):
    if n[-i]=='0':
        cnt+=1
    else : break

print(cnt)
