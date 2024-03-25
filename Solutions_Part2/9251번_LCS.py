w1=input() ; w2=input()
dp=[]
for _ in range(len(w2)+1):
    dp.append([0 for _ in range(len(w1)+1)])

for i in range(1, len(w2)+1):
    for j in range(1, len(w1)+1):
        if w2[i-1]==w1[j-1] : dp[i][j]=dp[i-1][j-1]+1
        else : dp[i][j]=max(dp[i-1][j], dp[i][j-1])

print(dp[len(w2)][len(w1)])
