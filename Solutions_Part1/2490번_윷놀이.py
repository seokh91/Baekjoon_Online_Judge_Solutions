import sys
info=['D', 'C', 'B', 'A', 'E']
a=[sum(list(map(int, sys.stdin.readline().split()))) for _ in range(3)]
for i in range(3):
    print(info[a[i]])
