import sys

n,k=list(map(int, sys.stdin.readline().split()))
m=[0 for _ in range(k+1)] ; m[0]=1
coin=[int(sys.stdin.readline().rstrip()) for _ in range(n)]

for i in coin :
    for j in range(1, k+1):
        if j >= i : m[j] += m[j-i]

print(m[k])
