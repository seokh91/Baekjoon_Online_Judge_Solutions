import sys

n=int(sys.stdin.readline().rstrip()) ; pibo=[0,1]
n%=1500000
for i in range(2, n+1):
    pibo.append(pibo[i-1]+pibo[i-2])
print(pibo[n]%(1000000))
