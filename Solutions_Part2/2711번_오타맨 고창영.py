n=int(input())
l=[]
for _ in range(n):
    a,b=input().split()
    l.append((int(a), b))

for i in l:
    result=''
    for j in range(len(i[1])):
        if j!=(i[0]-1) : result+=i[1][j]
    print(result)
