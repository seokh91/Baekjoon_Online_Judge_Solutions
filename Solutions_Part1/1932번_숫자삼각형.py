import sys
dp=[] ; n=int(input())
for i in range(n):
    temp=list(map(int, sys.stdin.readline().rstrip().split())) ; temp.append(0)
    if i==0 :
        dp.append(temp)
        continue
    for j in range(i+1):
        if j==0:
            temp[j]+=dp[i-1][0]
            continue
        temp[j]+=max(dp[i-1][j-1], dp[i-1][j])
    dp.append(temp)
print(max(dp[n-1]))
