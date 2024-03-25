import sys

str1=sys.stdin.readline().rstrip('\n')
str2=sys.stdin.readline().rstrip('\n')

mat=[] ; max_cnt=0
for _ in range(4000):
    mat.append([0]*4000)

for i in range(len(str2)):
    for j in range(len(str1)):
        if str2[i]==str1[j]:
            if i==0 or j==0 : mat[i][j]=1
            else : mat[i][j]=mat[i-1][j-1]+1
            if max_cnt < mat[i][j] : max_cnt=mat[i][j]

print(max_cnt)
