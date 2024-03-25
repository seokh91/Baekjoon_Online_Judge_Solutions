n=int(input())
dp=[] ; result=0
for _ in range(12):
    dp.append([0 for _ in range(n)])

for i in range(n):
    for j in range(1, 11):
        if i == 0 and j >= 2 : dp[j][i]=1
        else :
            dp[j][i]=dp[j+1][i-1]+dp[j-1][i-1]

for j in range(1, 11):
    result += dp[j][n-1]

print(result%1000000000)
