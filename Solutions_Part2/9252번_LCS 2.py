w1=input() ; w2=input()
dp=[]
for _ in range(len(w1)+1):
    dp.append([0 for _ in range(len(w2)+1)])

for i in range(1, len(w1)+1):
    for j in range(1, len(w2)+1):
        if w1[i-1]==w2[j-1] : dp[i][j]=dp[i-1][j-1]+1
        else : dp[i][j]=max(dp[i-1][j], dp[i][j-1])

result=dp[len(w1)][len(w2)]
print(result)

w3="" ; i=len(w1) ; j=len(w2)
while len(w3) != result :
    if w1[i-1] == w2[j-1] :
        w3=w1[i-1]+w3
        i-=1 ; j-=1
    else :
        if dp[i-1][j]==dp[i][j] : i-=1
        elif dp[i][j-1]==dp[i][j] : j-=1

print(w3)
