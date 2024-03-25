n=int(input())
pann=[0];location=[]

def basic(n,a,b):
    if n==3 :
        global pann
        pann[a][b]='*'
        pann[a+1][b+1]='*'
        pann[a+1][b-1]='*'
        pann[a+2][b]='*'
        pann[a+2][b+1]='*'
        pann[a+2][b-1]='*'
        pann[a+2][b+2]='*'
        pann[a+2][b-2]='*'
        return
    temp=n//2
    basic(temp,a,b)
    basic(temp,a+temp,b+temp)
    basic(temp,a+temp,b-temp)

for _ in range(n):
    pann.append([0]+[' ' for _ in range(n*2)])

basic(n,1,n)

for i in range(1,n+1):
    temp=''
    for j in range(1,2*n+1):
        temp+=pann[i][j]
    print(temp)
