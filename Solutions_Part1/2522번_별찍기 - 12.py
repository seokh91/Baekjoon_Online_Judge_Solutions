n=int(input())
for i in range(1,n+1):
    print(' '*(n-i), end=('*'*i))
    print()
for i in range(n-1,0,-1):
    print(' '*(n-i), end=('*'*i))
    print()
