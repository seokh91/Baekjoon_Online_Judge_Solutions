apart=[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]]
for _ in range(14):
    apart.append([0,1])
for i in range(1,15):
    for j in range(2, 15):
        apart[i].append(sum(apart[i-1][1:j+1]))
address=[]
n=int(input())
for _ in range(2*n):
    address.append(int(input()))
for i in range(0,2*n,2):
    print(apart[address[i]][address[i+1]])
