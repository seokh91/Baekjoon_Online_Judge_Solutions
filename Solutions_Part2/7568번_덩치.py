import sys

N=int(input()) ; inputs=[] ; result=[]

for i in range(N):
    inputs.append(list(map(int, sys.stdin.readline().rstrip('\n').split())))

for i in range(N):
    rank=1 ; weight=inputs[i][0] ; height=inputs[i][1]
    for j in range(N):
        if weight<inputs[j][0] and height<inputs[j][1] : rank+=1
    result.append(rank)

print(' '.join(map(str, result)))
