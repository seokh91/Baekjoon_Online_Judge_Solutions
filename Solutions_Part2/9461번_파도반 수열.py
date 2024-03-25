import sys
fado=[1,1,1,2,2,3]
n=int(input())
l=[int(sys.stdin.readline()) for _ in range(n)]
big=max(l)

if big-1 > 5:
    for i in range(big-6):
        fado.append(fado[len(fado)-1]+fado[len(fado)-5])
for i in l:
    print(fado[i-1])
