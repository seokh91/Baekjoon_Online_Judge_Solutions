n=int(input())
for i in range(n):
    print(' '*i, end=('*'*(2*n-1-2*i)))
    print()
for i in range(n-2,-1,-1):
    print(' '*i, end=('*'*(2*n-1-2*i)))
    print()
