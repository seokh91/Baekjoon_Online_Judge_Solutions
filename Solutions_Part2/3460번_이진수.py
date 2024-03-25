import sys
n=int(input())
l=[bin(int(sys.stdin.readline())) for i in range(n)]

for i in l:
    for j in range(len(i)-1, -1, -1):
        if i[j]=='1': print(len(i)-1-j, end=' ')
    print()
