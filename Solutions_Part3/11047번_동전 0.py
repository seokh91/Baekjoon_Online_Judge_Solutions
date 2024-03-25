import sys
n,k=input().split()
n=int(n); k=int(k)

a_l=[int(sys.stdin.readline()) for _ in range(n)]
a_l.sort(reverse=True)

result=0
for i in a_l :
    if i <= k :
        result+=k//i
        k%=i
        if k==0:
            print(result)
            break
