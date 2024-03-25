import sys
sites=[]
for _ in range(int(input())):
    sites.append(tuple(map(int,sys.stdin.readline().rstrip('\n').split())))

for i in sites:
    temp1=i[0] ; temp2=i[1]
    for j in range(1, i[0]):
        temp1*=(i[0]-j)
        temp2*=(i[1]-j)
    print(int(temp2/temp1))
