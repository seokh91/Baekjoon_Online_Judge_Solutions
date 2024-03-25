import sys
n=int(input())
seq=list(map(int, sys.stdin.readline().rstrip('\n').split()))
dp=[0 for _ in range(100010)]

for i in range(n):
    if i == 0 :
        dp[0]=seq[0]
    else :
        if dp[i-1] + seq[i] > seq[i] :
            dp[i]=dp[i-1]+seq[i]
        else :
            dp[i]=seq[i]

result=dp[0]
for i in range(1, n):
    if dp[i] > result : result=dp[i]

print(result)
