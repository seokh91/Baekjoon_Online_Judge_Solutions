n=int(input())
move=list(map(int, input().split()))
l=[]
for i in range(1,n+1):
    l.append(i)
for i in range(n):
    temp=l[i]
    for j in range(move[i]):
        l[i-j]=l[i-j-1]
    l[i-move[i]]=temp
for i in l : print(i, end=' ')
