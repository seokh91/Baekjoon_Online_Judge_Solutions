import sys
n=int(input())
l=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
gcd=lambda a,b : a if not b else gcd(b, a%b)

for i in l:
    i[0]=-1; i.sort(); result=[]
    for j in range(1, len(i)-1):
        for z in range(j+1, len(i)):
            result.append(gcd(i[j], i[z]))
    print(sum(result))
