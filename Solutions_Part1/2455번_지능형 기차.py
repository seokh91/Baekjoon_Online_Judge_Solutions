import sys
l=[tuple(map(int, sys.stdin.readline().split())) for _ in range(4)]
num_p=[]
num_p.append(l[0][1])
num_p.append(l[0][1]+l[1][1]-l[1][0])
num_p.append(l[0][1]+l[1][1]-l[1][0]+l[2][1]-l[2][0])
num_p.append(l[0][1]+l[1][1]-l[1][0]+l[2][1]-l[2][0]-l[3][0])

print(max(num_p))
