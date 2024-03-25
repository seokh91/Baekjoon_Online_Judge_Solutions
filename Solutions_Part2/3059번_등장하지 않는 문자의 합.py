import sys
n=int(input())
l=[sys.stdin.readline().rstrip('\n') for _ in range(n)]

for i in l:
    alpha=list('QWERTYUIOPASDFGHJKLZXCVBNM')
    for j in set(i):
        alpha.remove(j)
    result=0
    for z in alpha:
        result+=ord(z)
    print(result)
