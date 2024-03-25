def judge_min(a,b,c):
    if min(a,b,c)==999999:return 1
    else:return min(a,b,c)+1

n=int(input()) ; dp=[]
for _ in range(3):
    dp.append([999999 for _ in range(n)])

for i in range(n-1):
    if (n-i)%3==0 :
        dp[0][n-((n-i)//3)]=judge_min(dp[0][i], dp[1][i], dp[2][i])
    if (n-i)%2==0 :
        dp[1][n-((n-i)//2)]=judge_min(dp[0][i], dp[1][i], dp[2][i])
    if i<=n-2 :
        dp[2][i+1]=judge_min(dp[0][i], dp[1][i], dp[2][i])

if n==1 : print(0)
else : print(min(dp[0][n-1], dp[1][n-1], dp[2][n-1]))
