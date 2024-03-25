n,k=map(int, input().split())
l=[int(str(i*n)[::-1]) for i in range(1,k+1)]
print(max(l))
