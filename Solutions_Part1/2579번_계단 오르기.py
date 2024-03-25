import sys
n=int(input()) ; stairs=[] ; dp=[[],[]]
for _ in range(n):
    stairs.append(int(sys.stdin.readline().rstrip()))
    dp[0].append(0) ; dp[1].append(0)

dp[0][0]=stairs[0] ; dp[0][1]=stairs[0]+stairs[1] ; dp[1][1]=stairs[1]

for i in range(2, n):
    dp[0][i]=stairs[i]+dp[1][i-1]
    dp[1][i]=stairs[i]+max(dp[0][i-2], dp[1][i-2])

print(max(dp[0][n-1], dp[1][n-1]))
