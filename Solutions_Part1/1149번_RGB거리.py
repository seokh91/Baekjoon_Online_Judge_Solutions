import sys
dp=[] ; n=int(input())
for i in range(n):
    temp=list(map(int, sys.stdin.readline().rstrip().split()))
    if i==0:
        dp.append(temp)
        continue
    temp[0]+=min(dp[i-1][1], dp[i-1][2])
    temp[1]+=min(dp[i-1][0], dp[i-1][2])
    temp[2]+=min(dp[i-1][0], dp[i-1][1])
    dp.append(temp)
print(min(dp[n-1]))
